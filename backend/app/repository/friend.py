import typing as tp
import uuid

from sqlalchemy import select, delete

from .base import database, AsyncDatabaseSession
from .models.friend import Friend as FriendModel
from .models.user import User as UserModel
from .repository import FriendInterface
from ..domain import User, Friend


class FriendRepository(FriendInterface):
    def __init__(self, db: AsyncDatabaseSession = database):
        self.db = db

    async def create_friend(self, friend: Friend) -> None:
        f = FriendModel(
            user_id=friend.user_id,
            friend_id=friend.friend_id,
        )
        async with self.db.async_session() as session:
            session.add(f)
            await session.commit()
        return None

    async def get_friends(self, user_id: uuid.UUID) -> tp.List[User]:
        async with self.db.async_session() as session:
            result = await session.execute(
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
        async with self.db.async_session() as session:
            await session.execute(
                delete(FriendModel)
                .where(FriendModel.user_id == friend.user_id)
                .where(FriendModel.friend_id == friend.friend_id)
            )
            await session.commit()
        return None
