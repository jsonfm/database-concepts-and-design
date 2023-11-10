from fastapi import APIRouter

#schemas
from app.schemas.employers.forms import CreateEmployerForm, UpdateEmployerForm

router = APIRouter(prefix="/employers", tags=["Employers"])

@router.get("/")
def get_employers(limit: int = 30, offset: int = 0):
    return []

@router.get("/{employer_id}")
def get_employer(employer_id: int):
    return {}

@router.post("/")
def create_employer(form: CreateEmployerForm):
    return {}

@router.put("/")
def update_employer(form: UpdateEmployerForm):
    return {}

@router.delete("/{employer_id}")
def delete_employer(employer_id: int):
    return {}
