from fastapi import APIRouter

#
from app.models.users import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_users(limit: int = 50, offset: int = 0):
    return User.get_items(limit=limit, offset=offset)


@router.get("/profile/{user_id}")
def get_user_profile():
    return {}


@router.put("/profile/{user_id}")
def update_user_profile():
    return {}