from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from app.constants import TEMPLATES_DIR

templates = Jinja2Templates(directory=TEMPLATES_DIR)


def configure_templates_engine(app: FastAPI):
    return app


def render_template(name: str, context: dict = {}, status_code: int = 200):
    return templates.TemplateResponse(name, context, status_code=status_code)
