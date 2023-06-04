import abc
import uuid
import typing as tp

from ..domain import Post, PostEvent


class FeedInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def get_feed_by_user_id(
        self, user_id: uuid.UUID, limit: int
    ) -> tp.List[Post]:
        pass

    @abc.abstractmethod
    async def update_feed_by_user_id(
        self, user_id: uuid.UUID, posts: tp.List[Post]
    ) -> None:
        pass


class PostInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def handle_post(self, post_event: PostEvent) -> None:
        pass
