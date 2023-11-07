from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.constants import TEMPLATES_DIR

templates = Jinja2Templates(directory=TEMPLATES_DIR)


def configure_templates_engine(app: FastAPI):
    app.mount("/static", StaticFiles(directory="app/static"), name="static")

    return app


def render_template(
    request: Request, name: str, context: dict = {}, status_code: int = 200
):
    if context is None:
        context = {}
    context["request"] = request
    return templates.TemplateResponse(
        "pages/index.html", {"request": request}, status_code=status_code
    )
