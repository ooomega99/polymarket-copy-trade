from typing import Optional

from utils import CamelModel


class Position(CamelModel):
    proxy_wallet: Optional[str] = None
    asset: Optional[str] = None
    condition_id: Optional[str] = None
    size: Optional[float] = None
    avg_price: Optional[float] = None
    initial_value: Optional[float] = None
    current_value: Optional[float] = None
    cash_pnl: Optional[float] = None
    percent_pnl: Optional[float] = None
    total_bought: Optional[float] = None
    realized_pnl: Optional[float] = None
    percent_realized_pnl: Optional[float] = None
    cur_price: Optional[float] = None
    redeemable: Optional[bool] = None
    mergeable: Optional[bool] = None
    title: Optional[str] = None
    slug: Optional[str] = None
    icon: Optional[str] = None
    event_id: Optional[str] = None
    event_slug: Optional[str] = None
    outcome: Optional[str] = None
    outcome_index: Optional[int] = None
    opposite_outcome: Optional[str] = None
    opposite_asset: Optional[str] = None
    end_date: Optional[str] = None
    negative_risk: Optional[bool] = None

    def trader_url(self) -> str:
        if self.proxy_wallet is None:
            return ""
        return f"https://polymarket.com/{self.proxy_wallet}"

    def event_url(self) -> str:
        if self.event_slug is None:
            return ""
        return f"https://polymarket.com/event/{self.event_slug}"

    def event_url_markdown(self) -> str:
        if self.title is None:
            return ""
        return f"[{self.title}]({self.event_url()})"

