import uuid
from .usecase import ChatInterface
from backend.repository import ChatRepository, ChatRepoInterface


class ChatUsecase(ChatInterface):
    def __init__(self, repo: ChatRepoInterface = ChatRepository()):
        self.repo = repo

    async def create_chat(
        self, user_id: uuid.UUID, friend_id: uuid.UUID
    ) -> None:
        if not await self.repo.is_friend(user_id, friend_id):
            raise ValueError("Not friend")
