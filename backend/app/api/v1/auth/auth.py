import uuid

from fastapi import HTTPException

from app.usecase import AuthService
from app.usecase.auth import TokenData


def to_json_response(data: TokenData) -> dict:
    return {
        "message": "Login successfully",
        "data": {
            "access_token": data.access_token,
            "access_expires": data.access_expires,
            "token_type": data.token_type,
        },
    }


class AuthHandler:
    def __init__(self, auth_service: AuthService = AuthService()):
        self.auth_service = auth_service

    async def login(self, id_: uuid.UUID, password: str):
        try:
            data = await self.auth_service.access(id_, password)
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
        return to_json_response(data)
