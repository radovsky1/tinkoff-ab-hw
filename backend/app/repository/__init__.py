from .user import UserRepository, UserInterface as UserRepoInterface
from .friend import FriendRepository, FriendInterface as FriendRepoInterface
from .chat import ChatRepository, ChatInterface as ChatRepoInterface
from .post import PostRepository, PostInterface as PostRepoInterface

__all__ = [
    "UserRepository",
    "FriendRepository",
    "UserRepoInterface",
    "FriendRepoInterface",
    "ChatRepository",
    "ChatRepoInterface",
    "PostRepository",
    "PostRepoInterface",
]
