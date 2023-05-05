import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ.get("DATABASE_URL")


class AsyncDatabaseSession:
    def __init__(self):
        self._engine = create_async_engine(
            DATABASE_URL,
            future=True,
            echo=True,
        )
        self._session = sessionmaker(
            bind=self._engine,
            expire_on_commit=False,
            class_=AsyncSession,
        )()

    def __getattr__(self, name):
        return getattr(self._session, name)

    async def disconnect(self) -> None:
        if self._engine:
            await self._engine.dispose()


database = AsyncDatabaseSession()
