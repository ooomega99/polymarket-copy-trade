from typing import Optional

from pydantic import Field

from utils import CamelModel


class CreateMarketOrderResponse(CamelModel):
    error_msg: Optional[str] = None
    order_id: Optional[str] = Field(default=None, alias="orderID")
    taking_amount: Optional[str] = None
    status: Optional[str] = None
    transactions_hashes: Optional[list[str]] = None
    success: Optional[bool] = None

