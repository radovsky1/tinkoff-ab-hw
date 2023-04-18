import uuid

from fastapi import HTTPException
from starlette import status

from backend.domain import User
from backend.usecase import UserInterface, UserUsecase


class UserHandler:
    def __init__(self, usecase: UserInterface = UserUsecase()):
        self.usecase = usecase

    async def create_user(
        self, name: str, email: str, bio: str, password: str
    ) -> User:
        user = User(
            id=uuid.UUID(), name=name, email=email, bio=bio, password=password
        )
        try:
            await self.usecase.create_user(user)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
            )
        return user

    async def get_user_by_id(self, user_id: uuid.UUID) -> User:
        try:
            user = await self.usecase.get_user_by_id(user_id)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
            )
        return user

    async def get_users(self) -> list[User]:
        return await self.usecase.get_users()

    async def update_user(
        self,
        user_id: uuid.UUID,
        name: str,
        email: str,
        bio: str,
        password: str,
    ) -> User:
        user = User(
            id=user_id, name=name, email=email, bio=bio, password=password
        )
        try:
            await self.usecase.update_user(user)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
            )
        return user
