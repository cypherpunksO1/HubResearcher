from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import User


async def get_users(session: AsyncSession) -> list[User]:
    result = await session.execute(select(User))
    return result.scalars().all()


def add_user(session: AsyncSession, telegram_id: str):
    new_user = User(
        telegram_id=telegram_id
    )
    session.add(new_user)
    return new_user
