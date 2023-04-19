import abc
import uuid

from ..domain import User, Friend


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
