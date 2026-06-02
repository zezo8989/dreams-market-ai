from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum as SQLEnum
from datetime import datetime
from enum import Enum
from backend.app.models.base import BaseModel, TimestampMixin


class UserRole(str, Enum):
    """User role enum."""
    ADMIN = "admin"
    AUDITOR = "auditor"
    VIEWER = "viewer"


class User(BaseModel, TimestampMixin):
    """User model."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(SQLEnum(UserRole), default=UserRole.VIEWER, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    last_login = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
