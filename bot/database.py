import contextlib
from typing import AsyncIterator
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from bot import config, models  # noqa: F401  (модели нужны для регистрации таблиц)

engine = create_async_engine(config.DATABASE_URL, echo=False)
Session = async_sessionmaker(engine, expire_on_commit=False)


async def init_db() -> None:
    """Создать таблицы, если их ещё нет."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


@contextlib.asynccontextmanager
async def session_scope() -> AsyncIterator[Session]:
    """Unit-of-Work: commit/rollback в одном месте."""
    async with Session() as session:
        try:
            yield session
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            raise
