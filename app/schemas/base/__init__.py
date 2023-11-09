from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CustomBaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
    updated_at: datetime
    active: bool
    deleted: bool
