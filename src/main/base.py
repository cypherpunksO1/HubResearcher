from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from src.main.config import load_postgres_config
from sqlalchemy.orm import sessionmaker


pg_config = load_postgres_config()

DATABASE_URL = (
    "postgresql+asyncpg://%s:%s@%s/%s" % (
        pg_config.user,
        pg_config.password,
        pg_config.host,
        pg_config.db
    )
)


engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
