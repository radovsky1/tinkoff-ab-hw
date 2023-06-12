from fastapi import APIRouter

from .routes import (
    user_router,
    friend_router,
    auth_router,
    chat_router,
    post_router,
    admin_router,
)

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["Users"])
router.include_router(friend_router, prefix="/friends", tags=["Friends"])
router.include_router(auth_router, tags=["Auth"])
router.include_router(chat_router, prefix="/chats", tags=["Chats"])
router.include_router(post_router, prefix="/posts", tags=["Posts"])
router.include_router(admin_router, prefix="/admin", tags=["Admin"])

__all__ = ["router"]
