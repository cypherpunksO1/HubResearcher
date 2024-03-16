from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis import Redis

from src.main.config import (load_bot_config, 
                             load_redis_config, 
                             redis)

from src.presentation.telegram.start import start_router
from src.presentation.telegram.inline_search import inline_search_router


def get_dispatcher(bot: Bot) -> Dispatcher:
    storage = RedisStorage(
        redis=redis
    )
    dispatcher = Dispatcher(bot=bot)
    dispatcher.include_router(start_router)
    dispatcher.include_router(inline_search_router)
    
    return dispatcher
    

async def bot_main() -> None:
    config = load_bot_config()
    bot = Bot(config.bot_token)
    
    await get_dispatcher(bot).start_polling(bot)


