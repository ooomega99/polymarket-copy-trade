import json
import logging
from typing import List, Optional

from openai import OpenAI
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import MarketOrderArgs, OrderType
from py_clob_client.order_builder.constants import BUY, SELL
from py_order_utils.model import SignedOrder
from sqlalchemy import select, func

from api.models import MarketEvent
from config import ConfigGrok
from database import BuyPredictHistory, Session
from exceptions import PredictException
from models.create_market_order_response import CreateMarketOrderResponse
from predict.prompt import SYSTEM_PROMPT, USER_PROMPT

from api.models import PageEvent, Market
from api.polymarket_api import PolymarketApi


logger = logging.getLogger(__name__)

PURCHASE_AMOUNT_USD: int = 1
WHITELIST_TAGS = ["Tweet Markets", "Politics", "Elon Musk", "SpaceX", "Elections", "Trump", "Geopolitics"]


class PolymarketPredict:
    def __init__(self,
                 db: Session,
                 grok: ConfigGrok,
                 clob_client: ClobClient) -> None:
        self.db: Session = db
        self._ai: OpenAI = OpenAI(
            api_key=grok.api_key,
            base_url="https://api.x.ai/v1",
        )
        self._grok_model: str = grok.model
        self._temperature: float = grok.temperature

        self._clob: ClobClient = clob_client
        self._clob.set_api_creds(self._clob.create_or_derive_api_creds())

        self._poly_api: PolymarketApi = PolymarketApi()

    def analyze(self, market: Market) -> dict:
        event: MarketEvent = market.events[0]
        user_input: dict = {
            "title": event.title,
            "question": market.question,
            "description": market.description,
            "outcomes": market.outcomes,
        }

        user_prompt: str = USER_PROMPT % json.dumps(user_input)

        response = self._ai.chat.completions.create(
            model=self._grok_model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=self._temperature,
        )
        return json.loads(response.choices[0].message.content)

    def buy(self, asset_id: str, purchase_amount: int) -> CreateMarketOrderResponse:
        buy_args: MarketOrderArgs = MarketOrderArgs(
            token_id=asset_id,
            side=BUY,
            amount=purchase_amount,
        )

        signed_order: SignedOrder = self._clob.create_market_order(buy_args)
        raw_response: dict = self._clob.post_order(signed_order, OrderType.FAK)
        return CreateMarketOrderResponse(**raw_response)

    def new(self):
        for new in self._poly_api.new():
            # TODO: Temporary limit to avoid over trading
            count: int = self.db.execute(
                select(func.count()).select_from(BuyPredictHistory)
            ).scalar_one()
            if count >= 10:
                raise PredictException("Buy history reached limit, stopping further buys to avoid overtrading.")

            tag_labels = [new_tag.label for new_tag in new.tags if new_tag.label in WHITELIST_TAGS]
            if not tag_labels:
                continue

            new.markets.sort(key=lambda m: m.id)
            for market in new.markets:
                event: MarketEvent = market.events[0]
                exists = self.db.query(BuyPredictHistory).filter_by(
                    condition_id=market.condition_id,
                    event_slug=event.slug,
                ).first()
                if exists:
                    continue

                outcome_prices: List[str] = market.outcome_prices
                if any(float(price) > 0.65 for price in outcome_prices):
                    continue

                logger.info(f"Title: {new.title}")
                logger.info(f"Question: {market.question}")
                for outcome, price in zip(market.outcomes, outcome_prices):
                    logger.info(f"  Outcome: {outcome.upper()} at price {price}")

                result: dict = self.analyze(market)
                target_outcome: str = result.get("target_outcome", "N/A")
                confidence_score: float = result.get("confidence_score", 0.0)
                if target_outcome not in market.outcomes:
                    logger.info(">> Recommended outcome not in market outcomes, skipping buy.")
                    continue
                if confidence_score < 7.0:
                    logger.info(">> Confidence score too low, skipping buy.")
                    continue

                logger.info(f"Prediction Result >> Target Outcome: {target_outcome.upper()} | Score: {confidence_score}")

                asset_id: str = market.clob_token_ids[market.outcomes.index(target_outcome)]

                response = self.buy(asset_id, purchase_amount=PURCHASE_AMOUNT_USD)
                order_id: Optional[str] = response.order_id if bool(response.success) else None
                tx_hash: Optional[str] = response.transactions_hashes[0] \
                    if bool(response.success) and response.transactions_hashes else None

                if bool(response.success):
                    logger.info(
                        "BUY SUCCESS, Asset: [%s] %s Amount: %s | order ID: %s, Tx: %s",
                        asset_id,
                        event.slug,
                        PURCHASE_AMOUNT_USD,
                        order_id,
                        tx_hash,
                    )
                else:
                    logger.error(
                        "BUY FAILED, Asset: [%s] %s Amount: %s, message: %s",
                        asset_id,
                        event.slug,
                        PURCHASE_AMOUNT_USD,
                        response.error_msg,
                    )

                self.db.add(BuyPredictHistory(
                    asset_id=asset_id,
                    condition_id=market.condition_id,
                    event_slug=event.slug,
                    outcome=target_outcome,
                    order_id=order_id,
                    tx_hash=tx_hash,
                ))
                self.db.commit()

                logger.info("-" * 40)
                break

