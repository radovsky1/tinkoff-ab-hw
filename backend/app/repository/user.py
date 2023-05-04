import uuid

from .repository import UserInterface
from ..domain import User
from .base import BaseRepository, database


class UserRepository(UserInterface):
    def __init__(self, db: BaseRepository = database):
        self.db = db

    async def create_user(self, user: User) -> None:
        self.db.users.append(user)
        return None

    async def get_user_by_id(self, user_id: uuid.UUID) -> User:
        u = next((user for user in self.db.users if user.id == user_id), None)
        if u is None:
            raise ValueError("User not found")
        return u

    async def get_users(self) -> list[User]:
        return self.db.users

    async def update_user(self, user: User) -> None:
        for i, u in enumerate(self.db.users):
            if u.id == user.id:
                self.db.users[i] = user
                return None
        return None
