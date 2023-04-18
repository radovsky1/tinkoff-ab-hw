import uuid

from .usecase import UserInterface
from backend.domain import User
from backend.repository import UserRepository, UserRepoInterface


class UserUsecase(UserInterface):
    def __init__(self, repo: UserRepoInterface = UserRepository()):
        self.repo = repo

    async def create_user(self, user: User) -> None:
        return await self.repo.create_user(user)

    async def get_user_by_id(self, user_id: uuid.UUID) -> User:
        return await self.repo.get_user_by_id(user_id)

    async def get_users(self) -> list[User]:
        return await self.repo.get_users()

    async def update_user(self, user: User) -> None:
        return await self.repo.update_user(user)
