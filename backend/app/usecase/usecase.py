import abc
import uuid
import typing as tp

from ..domain import User, Friend, Post


class UserInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def create_user(self, user: User) -> None:
        pass

    @abc.abstractmethod
    async def get_user_by_id(self, user_id: uuid.UUID) -> User:
        pass

    @abc.abstractmethod
    async def get_users(self) -> list[User]:
        pass

    @abc.abstractmethod
    async def update_user(self, user: User) -> None:
        pass


class FriendInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def create_friend(self, friend: Friend) -> None:
        pass

    @abc.abstractmethod
    async def get_friends(self, user_id: uuid.UUID) -> list[User]:
        pass

    @abc.abstractmethod
    async def delete_friend(self, friend: Friend) -> None:
        pass


class ChatInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def create_chat(
        self, user_id: uuid.UUID, friend_id: uuid.UUID
    ) -> None:
        pass


class PostInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def create_post(self, post: Post) -> None:
        pass

    @abc.abstractmethod
    async def get_posts(self, user_id: uuid.UUID) -> tp.List[Post]:
        pass

    @abc.abstractmethod
    async def get_post_by_id(self, post_id: uuid.UUID) -> Post:
        pass
