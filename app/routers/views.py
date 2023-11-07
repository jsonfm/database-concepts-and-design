from fastapi import APIRouter

# utils
from app.utils.templates import render_template

router = APIRouter()


@router.get("/")
def home():
    return render_template("index.html")
