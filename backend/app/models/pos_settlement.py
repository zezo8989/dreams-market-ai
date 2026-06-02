from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum
from backend.app.models.base import BaseModel, TimestampMixin


class SettlementStatus(str, Enum):
    """Settlement status enum."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class POSSettlement(BaseModel, TimestampMixin):
    """POS Settlement model."""
    __tablename__ = "pos_settlements"

    id = Column(Integer, primary_key=True, index=True)
    batch_number = Column(String(50), nullable=False, index=True)
    terminal_id = Column(Integer, ForeignKey("terminals.id"), nullable=False, index=True)
    settlement_date = Column(DateTime, nullable=False, index=True)
    amount = Column(Float, nullable=False)
    currency = Column(String(3), default="EGP", nullable=False)
    transaction_count = Column(Integer, default=0)
    status = Column(SQLEnum(SettlementStatus), default=SettlementStatus.PENDING, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    terminal = relationship("Terminal", backref="settlements")
