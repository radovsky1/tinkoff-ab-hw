from fastapi import FastAPI

from .routers import init_routers
from .middleware import init_middlewares


def create_app() -> FastAPI:
    app = FastAPI()
    init_routers(app)
    init_middlewares(app)
    return app
