import json
import typing as tp
import uuid

from .base import rw, RwRedisRepository
from .repository import FeedInterface
from ..domain import Post


class FeedRepository(FeedInterface):
    def __init__(self, db: RwRedisRepository = rw):
        self.db = db

    async def get_feed_by_user_id(
        self, user_id: uuid.UUID, limit: int
    ) -> tp.List[Post]:
        posts = await self.db.get(str(user_id))  # bytes of list of dicts
        if posts is None:
            return []
        posts = json.loads(posts)  # list of dicts
        posts = [
            Post.from_dict(post) for post in posts
        ]  # list of Post objects
        return posts[:limit]

    async def set_feed_for_user(
        self, user_id: uuid.UUID, posts: tp.List[Post]
    ) -> None:
        posts = [post.to_dict() for post in posts]
        await self.db.set(str(user_id), json.dumps(posts))
