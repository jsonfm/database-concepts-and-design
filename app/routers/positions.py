from fastapi import APIRouter

#
from app.models.positions import ProfessionalPosition
# forms
from app.schemas.positions.forms import (CreateProfessionalPositionForm,
                                         UpdateProfessionalPositionForm)

router = APIRouter(prefix="/professional-positions", tags=["Professional Positions"])

@router.get("/")
def get_professional_positions(limit: int = 30, offset: int = 0):
    items = ProfessionalPosition.get_items(limit=limit, offset=offset)
    return items

@router.get("/{position_id}")
def get_professional_position(position_id: int):
    item = ProfessionalPosition.get_item(position_id)
    return item

@router.get("/user/{user_id}")
def get_professional_position_by_user(user_id: int):
    items = ProfessionalPosition.get_by_user_id(user_id)
    return items

@router.post("/")
def create_professional_position(form: CreateProfessionalPositionForm):
    item = ProfessionalPosition.create(form.dict())
    return item

@router.put("/")
def update_professional_position(form: UpdateProfessionalPositionForm):
    # item = ProfessionalPosition.update(form.dict())
    # return item
    print("form: ", form.dict())
    return {}

@router.delete("/{position_id}")
def delete_professional_position(position_id):
    result = ProfessionalPosition.delete(position_id)
    return result