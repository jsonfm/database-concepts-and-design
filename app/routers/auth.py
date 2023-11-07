from fastapi import APIRouter

from app.schemas.auth.forms import LoginForm, SignupForm

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(form: LoginForm):
    return {}


@router.post("/signup")
def signup(form: SignupForm):
    return {}
