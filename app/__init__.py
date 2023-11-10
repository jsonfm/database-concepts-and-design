from fastapi import FastAPI

from app.routers import router as router_api_v1
from app.routers.views import router as router_views
from app.utils.templates import configure_templates_engine


def get_app():
    app = FastAPI(title="💙 GTO API", description="This is the project related with the Course.", version="0.0.1")
    configure_templates_engine(app)
    app.include_router(router_api_v1)
    app.include_router(router_views)

    return app
