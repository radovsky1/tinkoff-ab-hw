import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import database, AsyncDatabaseSession
from .model import Friends as FriendModel
from .repository import ChatInterface


class ChatRepository(ChatInterface):
    def __init__(self, db: AsyncDatabaseSession = database):
        self.db = db

    async def is_friend(
            self, user_id: uuid.UUID, friend_id: uuid.UUID
    ) -> bool:
        result = await self.db.execute(
            select()
            .where(FriendModel.user_id == user_id)
            .where(FriendModel.friend_id == friend_id)
        )
        return result.scalars().first() is not None
