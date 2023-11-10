from pydantic import BaseModel


class ProfessionalPosition(BaseModel):
    id: int = Field(ge=1, examples=[1])
    user_id: int = Field(ge=1, examples=[1])
    job_title: str
    start_year: int = Field(ge=1900, le=2100, examples=[2000])
    end_year: Optional[int | None] = Field(ge=1900, le=2100, default=2005, examples=[2005, None])
