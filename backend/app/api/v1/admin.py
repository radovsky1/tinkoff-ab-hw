import typing as tp
import uuid

from app.domain import Post
from app.usecase import (
    PostInterface,
    PostUsecase,
    FriendInterface,
    FriendUsecase,
)
from fastapi import HTTPException
from starlette import status


class AdminHandler:
    def __init__(
        self,
        post_usecase: PostInterface = PostUsecase(),
        friend_usecase: FriendInterface = FriendUsecase(),
    ):
        self.post_usecase = post_usecase
        self.friend_usecase = friend_usecase

    async def get_post_by_id(self, post_id: uuid.UUID) -> Post:
        try:
            return await self.post_usecase.get_post_by_id(post_id)
        except Exception as err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(err),
            )

    async def get_friends_by_user_id(
        self, user_id: uuid.UUID
    ) -> tp.List[uuid.UUID]:
        try:
            friends = await self.friend_usecase.get_friends(user_id)
        except Exception as err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(err),
            )
        return [friend.id for friend in friends]

    async def get_posts_by_author_id(
        self, author_id: uuid.UUID
    ) -> tp.List[Post]:
        try:
            return await self.post_usecase.get_posts(author_id)
        except Exception as err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(err),
            )
