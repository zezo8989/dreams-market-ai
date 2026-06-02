from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app.models.base import BaseModel, TimestampMixin


class BankStatement(BaseModel, TimestampMixin):
    """Bank Statement model."""
    __tablename__ = "bank_statements"

    id = Column(Integer, primary_key=True, index=True)
    bank_name = Column(String(255), nullable=False, index=True)
    terminal_id = Column(Integer, ForeignKey("terminals.id"), nullable=False, index=True)
    deposit_date = Column(DateTime, nullable=False, index=True)
    amount = Column(Float, nullable=False)
    currency = Column(String(3), default="EGP", nullable=False)
    reference_number = Column(String(100), nullable=True, index=True)
    bank_reference = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    terminal = relationship("Terminal", backref="bank_statements")
