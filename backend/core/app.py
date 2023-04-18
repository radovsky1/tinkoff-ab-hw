from fastapi import FastAPI

from .routers import init_routers


def create_app() -> FastAPI:
    app = FastAPI()
    init_routers(app)
    return app
