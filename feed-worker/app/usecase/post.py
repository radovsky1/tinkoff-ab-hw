import os

from app.domain import PostEvent

from .adapters import BackendService
from .feed import FeedUsecase
from .usecase import PostInterface, FeedInterface


class PostUsecase(PostInterface):
    def __init__(
        self,
        feed_uc: FeedInterface = FeedUsecase(),
        backend_service: BackendService = BackendService(
            os.getenv('BACKEND_SERVICE_HOST')
        ),
    ):
        self.feed_uc = feed_uc
        self.backend_service = backend_service

    async def handle_post(self, post_event: PostEvent) -> None:
        post = self.backend_service.get_post_by_id(post_event.id)
        friends = self.backend_service.get_friends_by_user_id(post.author_id)
        for friend_id in friends:
            await self.feed_uc.update_feed_by_user_id(friend_id, [post])
