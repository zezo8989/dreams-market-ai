from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import declarative_mixin
from datetime import datetime
from backend.app.database import Base


@declarative_mixin
class TimestampMixin:
    """Mixin for timestamp fields."""
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class BaseModel(Base):
    """Base model with common fields."""
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
