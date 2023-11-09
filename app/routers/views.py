from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

# utils
from app.utils.templates import render_template, templates

router = APIRouter(include_in_schema=False)


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return render_template(request, "pages/index.html")


@router.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return render_template(request, "pages/login/index.html")


@router.get("/signup", response_class=HTMLResponse)
def signup(request: Request):
    return render_template(request, "pages/login/signup.html")
