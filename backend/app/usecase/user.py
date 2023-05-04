import uuid

from .usecase import UserInterface
from app.domain import User
from app.repository import UserRepository, UserRepoInterface
from passlib.context import CryptContext


class UserUsecase(UserInterface):
    def __init__(self, repo: UserRepoInterface = UserRepository()):
        self.repo = repo
        self.password_context = CryptContext(
            schemes=["bcrypt"], deprecated="auto"
        )

    def hash_password(self, password: str) -> str:
        return self.password_context.hash(password)

    async def create_user(self, user: User) -> None:
        user.password = self.hash_password(user.password)
        return await self.repo.create_user(user)

    async def get_user_by_id(self, user_id: uuid.UUID) -> User:
        return await self.repo.get_user_by_id(user_id)

    async def get_users(self) -> list[User]:
        return await self.repo.get_users()

    async def update_user(self, user: User) -> None:
        return await self.repo.update_user(user)
