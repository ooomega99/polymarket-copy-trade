from datetime import datetime, UTC
from sqlalchemy import Column, String, DateTime, Float

from .engine import Base


class BuyHistory(Base):
    __tablename__ = "buy_history"

    asset_id = Column(String, primary_key=True)
    condition_id = Column(String, primary_key=True)
    trader_address = Column(String, primary_key=True)

    threshold = Column(Float, primary_key=True)
    funder_address = Column(String, nullable=False)
    order_id = Column(String, nullable=True)
    tx_hash = Column(String, nullable=True)

    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
