import uuid
import os
import typing as tp

from .usecase import PostInterface
from app.domain import Post, PostEvent
from app.repository import PostRepository, PostRepoInterface
from ..amqp import Producer


class PostUsecase(PostInterface):
    def __init__(
        self,
        producer=Producer(os.getenv("AMQP_URL")),
        repo: PostRepoInterface = PostRepository(),
    ):
        self.producer = producer
        self.repo = repo

    async def create_post(self, post: Post) -> None:
        await self.repo.create_post(post)
        self.producer.publish(PostEvent(post.id, post.author_id))

    async def get_posts(self, user_id: uuid.UUID) -> tp.List[Post]:
        return await self.repo.get_posts(user_id)

    async def get_post_by_id(self, post_id: uuid.UUID) -> Post:
        return await self.repo.get_post_by_id(post_id)
