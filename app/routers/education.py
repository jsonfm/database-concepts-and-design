from fastapi import APIRouter

#
from app.models.education import Education
# froms
from app.schemas.education.forms import CreateEducationForm

router = APIRouter(prefix="/education", tags=["Education"])


@router.get("/")
def get_educations(limit: int = 50, offset: int = 0):
    items = Education.get_items(limit, offset)
    return items

@router.get("/{user_id}")
def get_educations_by_user(user_id: int):
    items = Education.get_by_user_id(user_id)
    return items

@router.get("/{education_id}")
def get_education(education_id):
    return {}


@router.post("/")
def create_education(form: CreateEducationForm):
    item = Education.create(form.dict())
    return item


@router.put("/")
def update_education():
    return {}


@router.delete("/")
def delete_education():
    return {}