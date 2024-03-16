from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram.types import Message
from aiogram.types import (InlineQuery,
                           InlineQueryResultArticle,
                           InputTextMessageContent,
                           InputMediaPhoto,
                           FSInputFile)
import os

from src.services import user_service
from src.main.base import get_session
from src.parsers import (get_repos_parser,
                         repo_image_parser)
from src.main.config import logger


search_repo_router = Router()


@search_repo_router.message()
async def message_search(
    message: Message
) -> None:

    repos = get_repos_parser.search_github_repos(
        query=message.text
    )
    if repos:
        repo = repos[0]
        repo_image_parser.save_repo_image(repo.name)

        await message.answer_photo(
            photo=FSInputFile(
                os.getenv("DEFAULT_IMAGES_DIR") + repo.name + ".png"
            ),
            caption=get_repos_parser.make_message(repo),
            reply_markup=get_repos_parser.get_repo_reply_markup(
                repo.url
            )
        )
    else:
        await message.answer(
            text="👀 Repo not found"
        )


@search_repo_router.inline_query()
async def inline_search(
    inline_query: InlineQuery
) -> None:
    repos = get_repos_parser.search_github_repos(
        query=inline_query.query
    )

    results: list[InlineQueryResultArticle] = list()
    
    for repo in repos:
        results.append(InlineQueryResultArticle(
            id=repo.name,
            title=repo.name,
            description=repo.description,
            input_message_content=InputTextMessageContent(
                message_text=get_repos_parser.make_message(repo=repo)
            ),
            reply_markup=get_repos_parser.get_repo_reply_markup(
                repo.url
            )
        ))

    await inline_query.answer(results, is_personal=True)
