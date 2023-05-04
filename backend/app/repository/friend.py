import uuid

from .repository import FriendInterface
from ..domain import User, Friend
from .base import BaseRepository, database


class FriendRepository(FriendInterface):
    def __init__(self, db: BaseRepository = database):
        self.db = db

    async def create_friend(self, friend: Friend) -> None:
        self.db.friends.append(friend)
        return None

    async def get_friends(self, user_id: uuid.UUID) -> list[User]:
        return [
            user
            for user in self.db.users
            if user.id
            in [
                friend.friend_id
                for friend in self.db.friends
                if friend.user_id == user_id
            ]
        ]

    async def delete_friend(self, friend: Friend) -> None:
        for i, f in enumerate(self.db.friends):
            if f.user_id == friend.user_id and f.friend_id == friend.friend_id:
                self.db.friends.pop(i)
                return None
        return None
