from typing import Optional

from pydantic import BaseModel, Field


class CreateEducationForm(BaseModel):
    user_id: int = Field(ge=1, examples=[1])
    title: str
    start_year: int = Field(ge=1900, le=2100, examples=[2000])
    end_year: Optional[int | None] = Field(ge=1900, le=2100, default=2005, examples=[2005, None])


class UpdateEducationForm(BaseModel):
    id: int = Field(ge=1, examples=[1], alias="education_id")
    title: Optional[str]
    start_year: int = Field(ge=1900, le=2100, examples=[2000])
    end_year: Optional[int | None] = Field(ge=1900, le=2100, default=2005, examples=[2005, None])
