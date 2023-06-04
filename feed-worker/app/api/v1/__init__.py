from fastapi import APIRouter

from .routes import feed_router

router = APIRouter()

router.include_router(feed_router, prefix="/feed", tags=["Feed"])

__all__ = ["router"]
