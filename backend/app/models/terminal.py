from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum
from backend.app.models.base import BaseModel, TimestampMixin


class TerminalStatus(str, Enum):
    """Terminal status enum."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"


class Terminal(BaseModel, TimestampMixin):
    """Terminal model."""
    __tablename__ = "terminals"

    id = Column(Integer, primary_key=True, index=True)
    tid = Column(String(50), unique=True, nullable=False, index=True)
    mid = Column(String(50), unique=True, nullable=False, index=True)
    bank_name = Column(String(255), nullable=False)
    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=False, index=True)
    status = Column(SQLEnum(TerminalStatus), default=TerminalStatus.ACTIVE, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    branch = relationship("Branch", backref="terminals")
