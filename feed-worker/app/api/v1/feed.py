import uuid
import typing as tp

from fastapi import HTTPException
from starlette import status

from app.domain import Post
from app.usecase import FeedInterface, FeedUsecase


class FeedHandler:
    def __init__(self, usecase: FeedInterface = FeedUsecase()):
        self.usecase = usecase

    async def get_feed_by_user_id(self, user_id: uuid.UUID) -> tp.List[Post]:
        try:
            return await self.usecase.get_feed_by_user_id(user_id)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
            )
