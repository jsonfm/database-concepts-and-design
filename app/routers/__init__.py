from fastapi import APIRouter

# routers
from app.routers.auth import router as router_auth
from app.routers.education import router as router_education
from app.routers.users import router as router_user

router = APIRouter(prefix="/api/v1")
router.include_router(router_auth)
router.include_router(router_user)
router.include_router(router_education)
