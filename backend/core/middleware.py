from fastapi import FastAPI

from backend.api.v1.auth.auth_backend import AuthBackend
from backend.core.middlewares.auth import AuthenticationMiddleware


def init_middlewares(app_: FastAPI) -> None:
    app_.add_middleware(
        AuthenticationMiddleware,
        backend=AuthBackend(
            prefix="/api/v1",
            endpoints=[
                "/friends/",
                "/chats/",
            ],
        ),
    )
