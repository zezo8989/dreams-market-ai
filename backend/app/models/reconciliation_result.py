from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum as SQLEnum, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum
from backend.app.models.base import BaseModel, TimestampMixin


class MatchStatus(str, Enum):
    """Match status enum."""
    MATCHED = "matched"
    MISSING_BANK_DEPOSIT = "missing_bank_deposit"
    MISMATCHED_AMOUNT = "mismatched_amount"
    DUPLICATE_BATCH = "duplicate_batch"
    UNMATCHED = "unmatched"


class ReconciliationResult(BaseModel, TimestampMixin):
    """Reconciliation Result model."""
    __tablename__ = "reconciliation_results"

    id = Column(Integer, primary_key=True, index=True)
    pos_settlement_id = Column(Integer, ForeignKey("pos_settlements.id"), nullable=False, index=True)
    bank_statement_id = Column(Integer, ForeignKey("bank_statements.id"), nullable=True)
    status = Column(SQLEnum(MatchStatus), nullable=False, index=True)
    amount_difference = Column(Float, default=0.0)
    date_difference_days = Column(Integer, default=0)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    pos_settlement = relationship("POSSettlement", backref="reconciliation_results")
    bank_statement = relationship("BankStatement", backref="reconciliation_results")
