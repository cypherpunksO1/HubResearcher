from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram.types import (InlineQuery,
                           InlineQueryResultPhoto,
                           InputMediaPhoto)


inline_search_router = Router()


@inline_search_router.inline_query()
async def inline_search(
    inline_query: InlineQuery
) -> None:
    results = [types.InlineQueryResultArticle(
        id='0',
        title='Text',
        input_message_content=types.InputTextMessageContent(
            message_text='Text')
    )]
    
    await inline_query.answer(results, is_personal=True)
