from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator


class DummyModel(BaseModel):
    """Example data model for validation."""

    id: str
    name: str
    email: Optional[str] = None
    age: Optional[int] = None
    created_at: datetime

    @field_validator("age")
    def age_must_be_over_18(cls, value):
        if value is not None and value < 18:
            raise ValueError("Age must be 18 or older.")
        return value

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat()}
