import uuid

from backend.domain import User, Friend
from .usecase import FriendInterface
from backend.repository import FriendRepository, FriendRepoInterface


class FriendUsecase(FriendInterface):
    def __init__(self, repo: FriendRepoInterface = FriendRepository()):
        self.repo = repo

    async def create_friend(self, friend: Friend) -> None:
        return await self.repo.create_friend(friend)

    async def get_friends(self, user_id: uuid.UUID) -> list[User]:
        return await self.repo.get_friends(user_id)

    async def delete_friend(self, friend: Friend) -> None:
        return await self.repo.delete_friend(friend)
