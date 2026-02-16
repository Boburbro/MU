import os
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:password@localhost:5432/simplechat",
)

engine = create_async_engine(DATABASE_URL, echo=False)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def run_migrations() -> None:
    # Lightweight migration to ensure new columns exist
    async with engine.begin() as conn:
        await conn.execute(
            text(
                "ALTER TABLE privatemessage ADD COLUMN IF NOT EXISTS read_at TIMESTAMP"
            )
        )
