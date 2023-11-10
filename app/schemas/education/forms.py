from typing import Optional

from pydantic import BaseModel, Field, model_validator


class CreateEducationForm(BaseModel):
    user_id: int = Field(ge=1, examples=[1])
    title: str
    start_year: int = Field(ge=1900, le=2100, examples=[2000])
    end_year: Optional[int | None] = Field(ge=1900, le=2100, default=2005, examples=[2005, None])

    @model_validator(mode="after")
    def validate_time_period(self, **kwargs):
        if self.end_year is not None:
            if self.end_year <= self.start_year:
                raise ValueError("`end_year` must be greater or equal than `start_year`")
        return self

class UpdateEducationForm(BaseModel):
    id: int = Field(ge=1, examples=[1], alias="education_id")
    title: Optional[str]
    start_year: int = Field(ge=1900, le=2100, examples=[2000])
    end_year: Optional[int | None] = Field(ge=1900, le=2100, default=2005, examples=[2005, None])

    @model_validator(mode="after")
    def validate_time_period(self, **kwargs):
        if self.end_year is not None:
            if self.end_year <= self.start_year:
                raise ValueError("`end_year` must be greater or equal than `start_year`")
        return self