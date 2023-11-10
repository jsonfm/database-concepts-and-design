from pydantic import BaseModel, Field


class CreateEmployerForm(BaseModel):
    name: str = Field(min_length=5)


class UpdateEmployerForm(BaseModel):
    employer_id: str = Field(min_value=1, alias="id")
    name: str = Field(min_length=5)