from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TerminalBase(BaseModel):
    tid: str = Field(..., min_length=1, max_length=50)
    mid: str = Field(..., min_length=1, max_length=50)
    bank_name: str = Field(..., min_length=1, max_length=255)
    branch_id: int


class TerminalCreate(TerminalBase):
    pass


class TerminalUpdate(BaseModel):
    bank_name: Optional[str] = None
    status: Optional[str] = None


class TerminalResponse(TerminalBase):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
