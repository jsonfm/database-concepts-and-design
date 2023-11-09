from datetime import datetime

from pydantic import BaseModel


class CustomBaseSchema(BaseModel):
    id: int
    created_at: datetime
    updated_now: datetime
    active: bool
    deleted: bool