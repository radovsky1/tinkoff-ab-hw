from fastapi import APIRouter

from .routes import user_router, friend_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["Users"])
router.include_router(friend_router, prefix="/friends", tags=["Friends"])

__all__ = ["router"]
