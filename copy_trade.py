import logging
from typing import Optional, Tuple

from py_clob_client.client import ClobClient
from py_clob_client.constants import POLYGON
from py_clob_client.order_builder.constants import BUY, SELL
from py_clob_client.clob_types import OrderType, MarketOrderArgs
from py_order_utils.model import SignedOrder

from config import ConfigTrader
from database import BuyHistory
from database.engine import Session

from exceptions import CopyTradeException

from api.polymarket_api import PolymarketApi
from api.models import Position, Activity, EventDetail, EventMarket
from models.create_market_order_response import CreateMarketOrderResponse

logger = logging.getLogger(__name__)


def _price_bounds(reference_price: float, slippage: int) -> Tuple[float, float]:
    """
    Compute lower and upper bounds based on a reference price and slippage percentage.
    Rounded to 2 decimal places.
    """
    if reference_price <= 0:
        raise CopyTradeException("Reference price must be positive")
    if not (0 < slippage < 100):
        raise CopyTradeException("Slippage must be in (0, 100)")

    lower = reference_price * (1 - slippage / 100)
    upper = reference_price * (1 + slippage / 100)

    return round(lower, 2), round(upper, 2)


class PolymarketCopyTrade:
    def __init__(
        self,
        db: Session,
        private_key: str,
        funder_address: str,
        percent_sell: Optional[int],
        traders: list[ConfigTrader],
    ) -> None:
        self.db: Session = db
        self.funder_address: str = funder_address
        self.percent_sell: Optional[int] = percent_sell
        self.traders: list[ConfigTrader] = traders

        # CLOB client configuration
        self.client: ClobClient = ClobClient(
            host="https://clob.polymarket.com",
            chain_id=POLYGON,
            signature_type=1,
            key=private_key,
            funder=funder_address,
        )
        self.client.set_api_creds(self.client.create_or_derive_api_creds())

        self.api: PolymarketApi = PolymarketApi()

    # ---------- Helpers ----------
    def _normalize_percent(self, percent_value: float) -> float:
        """
        Normalize percent value so returned value is percent (e.g. 5.0 for 5%).
        Handles both fractional (0.05) and percent (5) representations defensively.
        """
        if percent_value is None:
            return 0.0
        # If > 1, assume already percent (e.g. 5) otherwise assume fraction (0.05)
        return percent_value if percent_value > 1 else percent_value * 100.0

    def _get_market_price_for_side(self, market: EventMarket, side: str) -> float:
        """
        Return best price relevant to the action side.
        For BUY -> check best_ask/best_offer first.
        For SELL -> check best_bid first.
        Fallbacks used to be robust to different field names.
        """
        if side == BUY:
            price = getattr(market, "best_ask", None) or getattr(market, "best_offer", None)
        else:
            price = getattr(market, "best_bid", None)
        if price is None:
            # fallback to any available price field
            price = getattr(market, "price", None) or getattr(market, "mid_price", None)
        if price is None:
            raise CopyTradeException("Current market price unavailable for requested side")
        return price

    def _submit_market_order(
        self, args: MarketOrderArgs, order_type: OrderType
    ) -> CreateMarketOrderResponse:
        """
        Centralized submission & parsing of market orders. Handles exceptions and logs.
        """
        try:
            signed_order: SignedOrder = self.client.create_market_order(args)
            raw_response: dict = self.client.post_order(signed_order, order_type)
            response = CreateMarketOrderResponse(**raw_response)
            return response
        except Exception as e:
            logger.exception("Exception while creating/posting market order")
            raise CopyTradeException(f"Order submission failed: {e}") from e

    # ---------- Domain logic ----------
    def _get_event_market(self, position: Position) -> Tuple[EventDetail, EventMarket]:
        event: EventDetail = self.api.gamma.event.by_slug(position.event_slug)
        try:
            market: EventMarket = next(
                m for m in event.markets if m.condition_id == position.condition_id
            )
        except StopIteration:
            raise CopyTradeException("Market not found for given condition_id")

        # ensure some price present
        # allow either best_bid or best_ask depending on context; just assert at least one exists
        if (
            getattr(market, "best_bid", None) is None
            and getattr(market, "best_ask", None) is None
            and getattr(market, "best_offer", None) is None
        ):
            raise CopyTradeException("Current market price(s) missing or invalid")

        return event, market

    def sell_profit_positions(self) -> None:
        """
        Auto-sell positions held by the funder_address that exceed percent_sell threshold.
        """
        # nothing to do
        if not self.percent_sell:
            return

        funder_positions: list[Position] = self.api.data.core.positions(self.funder_address, limit=50)

        for position in funder_positions:
            # normalize percent_pnl to percent (e.g. 5.0)
            percent_pnl = self._normalize_percent(position.percent_pnl)
            if percent_pnl < self.percent_sell:
                continue

            sell_args: MarketOrderArgs = MarketOrderArgs(
                token_id=position.asset,
                side=SELL,
                amount=position.total_bought,
            )

            try:
                response = self._submit_market_order(sell_args, OrderType.FAK)
            except CopyTradeException:
                logger.error("Failed to submit sell order for asset %s", position.asset)
                continue

            if bool(response.success):
                logger.info("Success SELL, order ID: %s, asset: %s", response.order_id, position.asset)
                txs = response.transactions_hashes or []
                if txs:
                    logger.info("Tx: %s", txs[0])
            else:
                logger.error("Sell order failed: %s for position [%s] asset: %s",
                             response.error_msg, position.event_slug, position.asset)

    def buy(self, trader: ConfigTrader, position: Position) -> None:
        """
        Execute a buy order for a given trader and position.
        """

        # 1) Avoid duplicate buys (exact same trader/condition/asset/threshold/funder)
        exists = (
            self.db.query(BuyHistory)
            .filter_by(
                trader_address=trader.address,
                condition_id=position.condition_id,
                asset_id=position.asset,
                threshold=trader.threshold,
                funder_address=self.funder_address,
            )
            .first()
        )
        if exists:
            logger.info(
                "Position already bought, skipping. Trader: %s, Condition: %s, Asset: %s, Initial Value: %s",
                trader.address,
                position.condition_id,
                position.asset,
                position.initial_value,
            )
            return

        # 2) Fetch event and market
        try:
            event, market = self._get_event_market(position)
        except CopyTradeException as e:
            logger.error("Skipping buy, market lookup failed: %s", e)
            return

        # If event closed/ended, optionally record skipped buy
        if getattr(event, "closed", False) or getattr(event, "ended", False):
            # NOTE: consider adding a 'skipped' column to BuyHistory instead of inserting a normal buy
            record = BuyHistory(
                asset_id=position.asset,
                condition_id=position.condition_id,
                trader_address=trader.address,
                threshold=trader.threshold,
                funder_address=self.funder_address,
            )
            try:
                self.db.add(record)
                self.db.commit()
                logger.info("Event closed, recorded skipped buy and skipped. Outcome: [%s] %s", position.outcome, position.event_slug)
            except Exception:
                self.db.rollback()
                logger.exception("Failed to persist skipped BuyHistory")
            return

        # 3) Slippage check (use best ask for buy)
        try:
            if getattr(trader, "slippage", 0) and trader.slippage > 0:
                market_price = self._get_market_price_for_side(market, BUY)
                lower_bound, upper_bound = _price_bounds(position.avg_price, trader.slippage)
                if not (lower_bound <= market_price <= upper_bound):
                    raise CopyTradeException(
                        f"Current market price {market_price} outside of bounds ({lower_bound}, {upper_bound}), "
                        f"trader average price {position.avg_price}"
                    )
        except CopyTradeException as e:
            logger.warning("Slippage check failed, skipping buy for asset %s: %s", position.asset, e)
            return

        # 4) Submit buy order
        buy_args: MarketOrderArgs = MarketOrderArgs(
            token_id=position.asset,
            side=BUY,
            amount=trader.purchase_amount,
        )

        try:
            response = self._submit_market_order(buy_args, OrderType.FAK)
        except CopyTradeException:
            logger.error("Failed to submit buy order for asset %s", position.asset)
            return

        order_id: Optional[str] = response.order_id if bool(response.success) else None
        tx_hash: Optional[str] = None
        txs = getattr(response, "transactions_hashes", None) or []
        if txs:
            tx_hash = txs[0]

        if bool(response.success):
            logger.info(
                "BUY SUCCESS, Outcome: [%s] %s Amount: %s | order ID: %s, Tx: %s",
                position.outcome,
                position.event_slug,
                trader.purchase_amount,
                order_id,
                tx_hash,
            )
        else:
            logger.error(
                "BUY FAILED, Outcome: [%s] %s Amount: %s, message: %s",
                position.outcome,
                position.event_slug,
                trader.purchase_amount,
                response.error_msg,
            )
            return

        # 5) Persist buy history with transactional safety
        try:
            record = BuyHistory(
                asset_id=position.asset,
                condition_id=position.condition_id,
                trader_address=trader.address,
                threshold=trader.threshold,
                funder_address=self.funder_address,
                order_id=order_id,
                tx_hash=tx_hash,
            )
            self.db.add(record)
            self.db.commit()
        except Exception:
            logger.exception("Failed to save BuyHistory; rolling back.")
            self.db.rollback()

    def run(self) -> None:
        for trader in self.traders:
            try:
                positions: list[Position] = self.api.data.core.positions(address=trader.address)
            except Exception:
                logger.exception("Failed to fetch positions for trader %s", trader.address)
                continue

            for position in positions:
                if position.initial_value < trader.threshold:
                    continue
                try:
                    self.buy(trader, position)
                except Exception:
                    # avoid crashing whole run loop for a single position
                    logger.exception("Unhandled exception while processing buy for trader %s position %s",
                                     trader.address, getattr(position, "asset", "<unknown>"))

        # Sell profit positions if configured
        if self.percent_sell:
            try:
                self.sell_profit_positions()
            except Exception:
                logger.exception("Unhandled exception running sell_profit_positions")
