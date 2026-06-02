from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from backend.app.models.base import BaseModel, TimestampMixin


class Branch(BaseModel, TimestampMixin):
    """Branch model."""
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True, index=True)
    region = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
