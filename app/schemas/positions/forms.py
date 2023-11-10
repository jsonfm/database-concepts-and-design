from pydantic import BaseModel


class CreateProfessionalPositionForm(BaseModel):
    title: str


class UpdateProfessionalPositionForm(BaseModel):
    title: str