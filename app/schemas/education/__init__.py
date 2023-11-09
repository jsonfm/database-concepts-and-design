from typing import Optional

from pydantic import Field

from app.schemas.base import CustomBaseSchema


class Education(CustomBaseSchema):
    user_id: int
    title: str
    start_year: int
    end_year: Optional[int | None]
