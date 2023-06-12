import typing as tp
import uuid

from sqlalchemy import select

from .base import database, AsyncDatabaseSession
from .models.post import Post as PostModel
from .repository import PostInterface
from ..domain import Post


class PostRepository(PostInterface):
    def __init__(self, db: AsyncDatabaseSession = database):
        self.db = db

    async def create_post(self, post: Post) -> None:
        p = PostModel(
            id=post.id,
            author_id=post.author_id,
            content=post.content,
            created_at=post.created_at,
        )
        async with self.db.async_session() as session:
            session.add(p)
            await session.commit()
        return None

    async def get_posts(self, user_id: uuid.UUID) -> tp.List[Post]:
        async with self.db.async_session() as session:
            result = await session.execute(
                select(PostModel).where(PostModel.author_id == user_id)
            )
        posts = result.scalars().all()
        return [
            Post(
                id=post.id,
                author_id=post.author_id,
                content=post.content,
                created_at=post.created_at,
            )
            for post in posts
        ]

    async def get_post_by_id(self, post_id: uuid.UUID) -> Post:
        async with self.db.async_session() as session:
            result = await session.execute(
                select(PostModel).where(PostModel.id == post_id)
            )
        post = result.scalars().first()
        return Post(
            id=post.id,
            author_id=post.author_id,
            content=post.content,
            created_at=post.created_at,
        )
