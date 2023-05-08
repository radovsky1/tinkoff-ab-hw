from fastapi import FastAPI

from .routers import init_routers
from .middleware import init_middlewares
from prometheus_fastapi_instrumentator import Instrumentator


def create_app() -> FastAPI:
    app = FastAPI()
    init_routers(app)
    init_middlewares(app)
    Instrumentator().instrument(app).expose(app)
    return app
