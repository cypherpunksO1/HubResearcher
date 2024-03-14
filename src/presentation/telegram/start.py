from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram.types import Message


start_router = Router()


@start_router.message(CommandStart())
async def start(
    message: Message
) -> None:
    await message.answer(
        text="/testpool"
    )
