from fastapi import FastAPI

from app.routers import router as router_api_v1
from app.routers.views import router as router_views
from app.utils.templates import configure_templates_engine


def get_app():
    app = FastAPI()
    configure_templates_engine(app)
    app.include_router(router_api_v1)
    app.include_router(router_views)

    return app
