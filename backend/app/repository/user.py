import typing as tp
import uuid

from sqlalchemy import select, update
from datetime import datetime

from .base import database, AsyncDatabaseSession
from .models.user import User as UserModel
from .repository import UserInterface
from ..domain import User


class UserRepository(UserInterface):
    def __init__(self, db: AsyncDatabaseSession = database):
        self.db = db

    async def create_user(self, user: User) -> None:
        u = UserModel(
            id=user.id,
            name=user.name,
            email=user.email,
            bio=user.bio,
            password=user.password,
            last_login=datetime.now(),
        )
        self.db.add(u)
        await self.db.commit()
        await self.db.refresh(u)
        return None

    async def get_user_by_id(self, user_id: uuid.UUID) -> User:
        result = await self.db.execute(
            select(UserModel).where(UserModel.id == user_id)
        )
        user = result.scalars().first()
        if user is None:
            raise ValueError("No such user")
        return User(
            id=user.id,
            name=user.name,
            email=user.email,
            bio=user.bio,
            password=user.password,
        )

    async def get_users(self) -> tp.List[User]:
        result = await self.db.execute(select(UserModel))
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

    async def update_user(self, user: User) -> None:
        await self.db.execute(
            update(UserModel)
            .where(UserModel.id == user.id)
            .values(
                name=user.name,
                email=user.email,
                bio=user.bio,
                password=user.password,
            )
        )
        await self.db.commit()
        return None

    async def update_last_login(self, user_id: uuid.UUID) -> None:
        await self.db.execute(
            update(UserModel)
            .where(UserModel.id == user_id)
            .values(last_login=datetime.now())
        )
        return None
