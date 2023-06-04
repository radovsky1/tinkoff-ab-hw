from fastapi import APIRouter
from fastapi import status

from .chat import ChatHandler
from .friend import FriendHandler
from .user import UserHandler
from .auth import AuthHandler
from .post import PostHandler
from .admin import AdminHandler

user_handler = UserHandler()
friend_handler = FriendHandler()
auth_handler = AuthHandler()
chat_handler = ChatHandler()
post_handler = PostHandler()
admin_handler = AdminHandler()

user_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

user_router.add_api_route(
    path="/",
    endpoint=user_handler.get_users,
    methods=["GET"],
    status_code=status.HTTP_200_OK,
    description="Get all users",
    name="Get all users",
    response_model_by_alias=False,
)

user_router.add_api_route(
    path="/",
    endpoint=user_handler.create_user,
    methods=["POST"],
    status_code=status.HTTP_201_CREATED,
    description="Create a user",
    name="Create a user",
    response_model_by_alias=False,
)

user_router.add_api_route(
    path="/{user_id}",
    endpoint=user_handler.get_user_by_id,
    methods=["GET"],
    status_code=status.HTTP_200_OK,
    description="Get a user by id",
    name="Get a user by id",
    response_model_by_alias=False,
)

user_router.add_api_route(
    path="/{user_id}",
    endpoint=user_handler.update_user,
    methods=["PUT"],
    status_code=status.HTTP_200_OK,
    description="Update a user by id",
    name="Update a user by id",
    response_model_by_alias=False,
)

friend_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

friend_router.add_api_route(
    path="/",
    endpoint=friend_handler.create_friend,
    methods=["POST"],
    status_code=status.HTTP_201_CREATED,
    description="Create a friend",
    name="Create a friend",
    response_model_by_alias=False,
)

friend_router.add_api_route(
    path="/{user_id}",
    endpoint=friend_handler.get_friends,
    methods=["GET"],
    status_code=status.HTTP_200_OK,
    description="Get friends by user id",
    name="Get friends by user id",
    response_model_by_alias=False,
)

friend_router.add_api_route(
    path="/",
    endpoint=friend_handler.delete_friend,
    methods=["DELETE"],
    status_code=status.HTTP_200_OK,
    description="Delete a friend",
    name="Delete a friend",
    response_model_by_alias=False,
)

auth_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

auth_router.add_api_route(
    path="/login",
    endpoint=auth_handler.login,
    methods=["POST"],
    description="Login",
    name="Login",
    response_model_by_alias=False,
)

chat_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

chat_router.add_websocket_route(
    path="/ws/{user_id}/{friend_id}",
    endpoint=chat_handler.create_chat,
    name="Create a chat",
)

post_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

post_router.add_api_route(
    path="/",
    endpoint=post_handler.create_post,
    methods=["POST"],
    status_code=status.HTTP_201_CREATED,
    description="Create a post",
    name="Create a post",
    response_model_by_alias=False,
)

post_router.add_api_route(
    path="/author/{user_id}",
    endpoint=post_handler.get_posts,
    methods=["GET"],
    status_code=status.HTTP_200_OK,
    description="Get posts by user id",
    name="Get posts by user id",
    response_model_by_alias=False,
)

post_router.add_api_route(
    path="/{post_id}",
    endpoint=post_handler.get_post_by_id,
    methods=["GET"],
    status_code=status.HTTP_200_OK,
    description="Get a post by id",
    name="Get a post by id",
    response_model_by_alias=False,
)

admin_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

admin_router.add_api_route(
    path="/posts/{post_id}",
    endpoint=admin_handler.get_post_by_id,
    methods=["GET"],
    status_code=status.HTTP_200_OK,
    description="Get a post by id",
    name="Get a post by id",
    response_model_by_alias=False,
)

admin_router.add_api_route(
    path="/friends/{user_id}",
    endpoint=admin_handler.get_friends_by_user_id,
    methods=["GET"],
    status_code=status.HTTP_200_OK,
    description="Get friends by user id",
    name="Get friends by user id",
    response_model_by_alias=False,
)

admin_router.add_api_route(
    path="/posts/author/{author_id}",
    endpoint=admin_handler.get_posts_by_author_id,
    methods=["GET"],
    status_code=status.HTTP_200_OK,
    description="Get posts by author id",
    name="Get posts by author id",
    response_model_by_alias=False,
)
