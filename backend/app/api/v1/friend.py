import uuid

from fastapi import HTTPException
from starlette import status

from app.domain import User, Friend
from app.usecase import FriendInterface, FriendUsecase


class FriendHandler:
    def __init__(self, usecase: FriendInterface = FriendUsecase()):
        self.usecase = usecase

    async def create_friend(
        self, user_id: uuid.UUID, friend_id: uuid.UUID
    ) -> None:
        friend = Friend(user_id=user_id, friend_id=friend_id)
        try:
            await self.usecase.create_friend(friend)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
            )
        return None

    async def get_friends(self, user_id: uuid.UUID) -> list[User]:
        try:
            friends = await self.usecase.get_friends(user_id)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
            )
        return friends

    async def delete_friend(
        self, user_id: uuid.UUID, friend_id: uuid.UUID
    ) -> None:
        friend = Friend(user_id=user_id, friend_id=friend_id)
        try:
            await self.usecase.delete_friend(friend)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
            )
        return None
