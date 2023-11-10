from fastapi import APIRouter, HTTPException, status

#
from app.routers.users import User as UserRepository
# schemas
from app.schemas.auth.forms import LoginForm, SignupForm
from app.schemas.users import User
# utils
from app.utils.auth import create_access_token, verify_password

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(form: LoginForm):
    user = UserRepository.get_by_email(form.email)

    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="user doesn't exist")

    if not verify_password(form.password, user.password):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="password is incorrect")

    token = create_access_token(form.email)
    data = { "access_token": token }
    return data


@router.post("/signup")
def signup(form: SignupForm):
    data = form.dict() # validated form with hashed password
    user = UserRepository.create(data)
    return {"message": "user registered!"}