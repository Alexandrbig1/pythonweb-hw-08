import contextlib
import logging
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.conf.config import settings

logger = logging.getLogger("uvicorn.error")


class DatabaseSessionNotInitializedError(Exception):
    pass


class DatabaseSessionManager:
    def __init__(self, url: str):
        self._engine: AsyncEngine | None = create_async_engine(
            url,
            pool_size=10,  
            max_overflow=20,
        )
        self._session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
            autoflush=False, autocommit=False, bind=self._engine
        )

    @contextlib.asynccontextmanager
    async def session(self):
        if self._session_maker is None:
            raise DatabaseSessionNotInitializedError("Database session is not initialized")
        session = self._session_maker()
        try:
            yield session
        except SQLAlchemyError as e:
            logger.error(f"Database error: {e}")
            await session.rollback()
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}", exc_info=True)
            await session.rollback()
            raise
        finally:
            await session.close()


sessionmanager = DatabaseSessionManager(settings.DB_URL)


async def get_db():
    async with sessionmanager.session() as session:
        yield session


async def test_connection():
    engine = create_async_engine("postgresql+asyncpg://postgres:873752@localhost:5432/contacts_db")
    async with engine.connect() as conn:
        print("Connection successful!")

asyncio.run(test_connection())