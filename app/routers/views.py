from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

# utils
from app.utils.templates import render_template, templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return render_template(request, "pages/index.html")
