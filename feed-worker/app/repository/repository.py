import abc
import uuid
import typing as tp

from ..domain import Post


class FeedInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def get_feed_by_user_id(
        self, user_id: uuid.UUID, limit: int
    ) -> tp.List[Post]:
        pass

    @abc.abstractmethod
    async def set_feed_for_user(
        self, user_id: uuid.UUID, posts: tp.List[Post]
    ) -> None:
        pass
