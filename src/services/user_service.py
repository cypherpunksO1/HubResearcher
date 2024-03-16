from sqlalchemy import select
from src.main.base import Session
from src.models import User


async def get_users(session: Session) -> list[User]:
    result = await session.execute(select(User))
    return result.scalars().all()


def add_user(session: Session, telegram_id: str):
    new_user = User(
        telegram_id=telegram_id
    )
    session.add(new_user)
    session.commit()
    
    return new_user
