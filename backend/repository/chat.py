import uuid

from .base import BaseRepository, database
from .repository import ChatInterface


class ChatRepository(ChatInterface):
    def __init__(self, db: BaseRepository = database):
        self.db = db

    async def is_friend(
        self, user_id: uuid.UUID, friend_id: uuid.UUID
    ) -> bool:
        return any(
            [
                friend.user_id == user_id and friend.friend_id == friend_id
                for friend in self.db.friends
            ]
        )
