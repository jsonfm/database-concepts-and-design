from typing import Optional

from pydantic import BaseModel, Field


class CreateProfessionalPositionForm(BaseModel):
    job_title: str
    user_id: int = Field(ge=1, examples=[1])
    start_year: int = Field(ge=1900, le=2100, examples=[2000])
    end_year: Optional[int | None] = Field(ge=1900, le=2100, default=2005, examples=[2005, None])



class UpdateProfessionalPositionForm(BaseModel):
    id: int = Field(ge=1, alias="professional_position_id", description="professional position id", examples=[1])
    job_title: str
    start_year: int = Field(ge=1900, le=2100, examples=[2000])
    end_year: Optional[int | None] = Field(ge=1900, le=2100, default=2005, examples=[2005, None])
