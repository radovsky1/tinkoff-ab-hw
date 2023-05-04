from .user import UserRepository, UserInterface as UserRepoInterface
from .friend import FriendRepository, FriendInterface as FriendRepoInterface

__all__ = [
    "UserRepository",
    "FriendRepository",
    "UserRepoInterface",
    "FriendRepoInterface",
]
