import typing as tp
import uuid

from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from .base import database, AsyncDatabaseSession
from .model import Friends as FriendModel, Users as UserModel
from .repository import FriendInterface
from ..domain import User, Friend


class FriendRepository(FriendInterface):
    def __init__(self, db: AsyncDatabaseSession = database):
        self.db = db

    async def create_friend(self, friend: Friend) -> None:
        f = FriendModel(user_id=friend.user_id, friend_id=friend.friend_id)
        self.db.add(f)
        await self.db.commit()
        await self.db.refresh(f)
        return None

    async def get_friends(self, user_id: uuid.UUID) -> tp.List[User]:
        result = await self.db.execute(
            select(UserModel)
            .join(FriendModel, UserModel.id == FriendModel.friend_id)
            .where(FriendModel.user_id == user_id)
        )
        users = result.scalars().all()
        return [
            User(
                id=user.id,
                name=user.name,
                email=user.email,
                bio=user.bio,
                password=user.password,
            )
            for user in users
        ]

    async def delete_friend(self, friend: Friend) -> None:
        await self.db.execute(
            delete(FriendModel)
            .where(FriendModel.user_id == friend.user_id)
            .where(FriendModel.friend_id == friend.friend_id)
        )
        await self.db.commit()
        return None
