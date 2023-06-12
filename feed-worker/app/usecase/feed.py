import uuid
import typing as tp

from .usecase import FeedInterface
from app.domain import Post
from app.repository import FeedRepository

FEED_SIZE = 500


class FeedUsecase(FeedInterface):
    def __init__(self, repo: FeedRepository = FeedRepository()):
        self.repo = repo

    async def update_feed_by_user_id(
        self, user_id: uuid.UUID, posts: tp.List[Post]
    ) -> None:
        old_posts = await self.repo.get_feed_by_user_id(user_id, FEED_SIZE)
        new_posts = old_posts + posts
        await self.repo.set_feed_for_user(user_id, new_posts)

    async def get_feed_by_user_id(
        self, user_id: uuid.UUID, limit: int = FEED_SIZE
    ) -> tp.List[Post]:
        posts = await self.repo.get_feed_by_user_id(user_id, limit)
        return posts
