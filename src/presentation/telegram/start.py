from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram.types import Message

from src.services import user_service
from src.main.base import get_session


start_router = Router()

@start_router.message(CommandStart())
async def start(
    message: Message
) -> None:

    user_service.add_user(
        session=get_session(),
        telegram_id=message.from_user.id
    )

    await message.answer(
        text="/testpool"
    )
