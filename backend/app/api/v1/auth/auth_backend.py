from typing import Tuple, Union, List

from fastapi.security.utils import get_authorization_scheme_param
from starlette.authentication import (
    AuthenticationBackend,
    UnauthenticatedUser,
)
from starlette.requests import HTTPConnection

from app.core.schemas.base import BaseAuthenticationError
from app.domain import User
from app.usecase.auth import AuthService


class CustomAuthenticationError(BaseAuthenticationError):
    status = "error"
    status_type = "authentication"
    message = "Invalid token"
    _status_code = 401


class AuthBackend(AuthenticationBackend):
    def __init__(
        self,
        prefix: str,
        endpoints: List[str],
        auth_service: AuthService = AuthService(),
    ):
        self.prefix = prefix
        self.endpoints = endpoints
        self.auth_service = auth_service

    async def authenticate(
        self, conn: HTTPConnection
    ) -> Tuple[bool, Union[User, UnauthenticatedUser]]:
        cur_path = conn.url.path.removeprefix(self.prefix)

        if cur_path not in self.endpoints:
            return False, UnauthenticatedUser()

        authorization = conn.headers.get("Authorization")
        if not authorization:
            raise CustomAuthenticationError
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            raise CustomAuthenticationError
        try:
            user = await self.auth_service.get_user_from_access_token(param)
            conn.scope["user"] = user
        except ValueError:
            raise CustomAuthenticationError

        return True, user
