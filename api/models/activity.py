from datetime import datetime
from typing import Optional

from utils import CamelModel


class Activity(CamelModel):
    proxy_wallet: Optional[str] = None
    timestamp: Optional[datetime] = None
    condition_id: Optional[str] = None
    type: Optional[str] = None
    size: Optional[float] = None
    usdc_size: Optional[float] = None
    transaction_hash: Optional[str] = None
    price: Optional[float] = None
    asset: Optional[str] = None
    side: Optional[str] = None
    outcome_index: Optional[int] = None
    title: Optional[str] = None
    slug: Optional[str] = None
    icon: Optional[str] = None
    event_slug: Optional[str] = None
    outcome: Optional[str] = None
    name: Optional[str] = None
    pseudonym: Optional[str] = None

    def trader_url(self) -> str:
        if self.proxy_wallet is None:
            return ""
        return f"https://polymarket.com/{self.proxy_wallet}"

    def trader_url_markdown(self) -> str:
        if self.name is None:
            return ""
        return f"[{self.name}]({self.trader_url()})"

    def event_url(self) -> str:
        if self.event_slug is None:
            return ""
        return f"https://polymarket.com/event/{self.event_slug}"

    def event_url_markdown(self) -> str:
        if self.title is None:
            return ""
        return f"[{self.title}]({self.event_url()})"

    def transaction_url(self) -> str:
        if self.transaction_hash is None:
            return ""
        return f"https://polygonscan.com/tx/{self.transaction_hash}"

