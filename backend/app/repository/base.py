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
        self.async_session = sessionmaker(
            self._engine, class_=AsyncSession, expire_on_commit=False
        )


database = AsyncDatabaseSession()
