from fastapi import APIRouter
from fastapi import status

from .feed import FeedHandler

feed_handler = FeedHandler()

feed_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

feed_router.add_api_route(
    path="/{user_id}",
    endpoint=feed_handler.get_feed_by_user_id,
    methods=["GET"],
    status_code=status.HTTP_200_OK,
    description="Get a feed by user id",
    name="Get a feed by user id",
    response_model_by_alias=False,
)
