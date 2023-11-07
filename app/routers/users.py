from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_users(limit: int = 50, offset: int = 0):
    return []
