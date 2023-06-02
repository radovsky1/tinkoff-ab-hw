import typing as tp
import uuid
from datetime import datetime

from sqlalchemy import select, update

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
        )
        async with self.db.async_session() as session:
            session.add(u)
            await session.commit()
        return None

    async def get_user_by_id(self, user_id: uuid.UUID) -> User:
        async with self.db.async_session() as session:
            result = await session.execute(
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
        async with self.db.async_session() as session:
            result = await session.execute(select(UserModel))
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
        async with self.db.async_session() as session:
            await session.execute(
                update(UserModel)
                .where(UserModel.id == user.id)
                .values(
                    name=user.name,
                    email=user.email,
                    bio=user.bio,
                    password=user.password,
                )
            )
            await session.commit()
        return None

    async def update_last_login(self, user_id: uuid.UUID) -> None:
        async with self.db.async_session() as session:
            await session.execute(
                update(UserModel)
                .where(UserModel.id == user_id)
                .values(last_login=datetime.now())
            )
        return None
