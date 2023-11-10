from typing import Optional

from pydantic import BaseModel, Field


class CreateEducationForm(BaseModel):
    title: str
    user_id: int = Field(min_value=1)
    start_year: int = Field(..., min_value=1900, max_value=2100)
    end_year: Optional[int | None] = Field(min_value=1900, max_value=2100, default=None)


class UpdateEducationForm(BaseModel):
    title: Optional[str]
    start_year: Optional[int] = Field(..., min_value=1900, max_value=2100)
    end_year: Optional[int | None] = Field(min_value=1900, max_value=2100, default=None)