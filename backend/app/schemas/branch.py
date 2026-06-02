from pydantic import BaseModel, Field
from datetime import datetime


class BranchBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    region: str = Field(..., min_length=1, max_length=255)


class BranchCreate(BranchBase):
    pass


class BranchUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    region: str = Field(..., min_length=1, max_length=255)


class BranchResponse(BranchBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
