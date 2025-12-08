from datetime import datetime, UTC
from sqlalchemy import Column, String, DateTime, Float

from .engine import Base


class BuyPredictHistory(Base):
    __tablename__ = "buy_predict_history"

    asset_id = Column(String, primary_key=True)
    condition_id = Column(String, primary_key=True)
    event_slug = Column(String, nullable=False)

    outcome = Column(String, nullable=False)
    order_id = Column(String, nullable=True)
    tx_hash = Column(String, nullable=True)

    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
