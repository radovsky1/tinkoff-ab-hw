import os
import uuid
from datetime import datetime, timedelta

import jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from backend.domain import User
from backend.repository import UserRepository


class TokenData(BaseModel):
    access_token: str
    access_expires: int
    token_type: str = "Bearer"


class TokenPayload(BaseModel):
    sub: int
    name: str


class AuthService:
    def __init__(self, user_repo: UserRepository = UserRepository()):
        self.user_repo = user_repo
        self.password_context = CryptContext(
            schemes=["bcrypt"], deprecated="auto"
        )

    def hash_password(self, password: str) -> str:
        return self.password_context.hash(password)

    def verify_password(
        self, plain_password: str, hashed_password: str
    ) -> bool:
        return self.password_context.verify(plain_password, hashed_password)

    async def create_token_data_from_user(self, user: User) -> TokenData:
        payload = TokenPayload(sub=user.id, name=user.name)

        return TokenData(
            access_token=await self.create_access_token(payload),
            access_expires=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)),
        )

    async def create_access_token(self, payload: TokenPayload):
        return jwt.encode(
            payload={
                **payload.dict(),
                "exp": datetime.utcnow()
                + timedelta(
                    minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
                ),
            },
            key=os.getenv("JWT_ACCESS_SECRET_KEY", "secret"),
            algorithm=os.getenv("JWT_ALGORITHM", "HS256"),
        )

    async def access(self, id_: uuid.UUID, password: str) -> TokenData:
        user = await self.user_repo.get_user_by_id(id_)
        if user is None:
            raise ValueError("User not found")
        if not self.verify_password(password, user.password):
            raise ValueError("Incorrect password")

        return await self.create_token_data_from_user(user)

    async def decode_access_token(self, token: str) -> dict:
        try:
            return jwt.decode(
                token,
                key=os.getenv("JWT_ACCESS_SECRET_KEY", "secret"),
                algorithms=[os.getenv("JWT_ALGORITHM", "HS256")],
            )
        except jwt.exceptions.DecodeError:
            raise ValueError("Invalid token")
        except jwt.exceptions.ExpiredSignatureError:
            raise ValueError("Token expired")

    async def get_user_from_access_token(self, token: str) -> User:
        decoded_token = await self.decode_access_token(token)
        user = await self.user_repo.get_user_by_id(decoded_token["sub"])
        if user is None:
            raise ValueError("User not found")

        return user
