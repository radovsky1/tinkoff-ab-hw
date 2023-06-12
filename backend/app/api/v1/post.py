import uuid
import typing as tp

from fastapi import HTTPException
from starlette import status
from datetime import datetime

from app.domain import Post
from app.usecase import PostInterface, PostUsecase


class PostHandler:
    def __init__(self, usecase: PostInterface = PostUsecase()):
        self.usecase = usecase

    async def create_post(self, user_id: uuid.UUID, content: str) -> Post:
        post = Post(
            id=uuid.uuid4(),
            author_id=user_id,
            content=content,
            created_at=datetime.now(),
        )
        try:
            await self.usecase.create_post(post)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
            )
        return post

    async def get_posts(self, user_id: uuid.UUID) -> tp.List[Post]:
        try:
            posts = await self.usecase.get_posts(user_id)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
            )
        return posts

    async def get_post_by_id(self, post_id: uuid.UUID) -> Post:
        try:
            return await self.usecase.get_post_by_id(post_id)
        except Exception as err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(err),
            )
