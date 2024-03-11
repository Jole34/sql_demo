from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserOut(BaseModel):
    id: int
    email: EmailStr
    class Config:
        from_attributes = True


class UpdateUser(BaseModel):
    budget: Optional[float] = None
    name: Optional[str] = None


