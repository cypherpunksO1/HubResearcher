import requests
import pprint
from bs4 import BeautifulSoup
from dataclasses import dataclass
from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup)

from src.parsers.exceptions import *


@dataclass
class Repo:
    url: str | None = None
    archived: bool = False
    followers: int = 0
    name: str | None = None
    description: str | None = None
    repo_id: int | None = None
    language: str = "python"
    is_public: bool = True
    last_updated: str | None = None
    sponsorable: bool = False
    topics: list[str] | None = None


def make_message(repo: Repo) -> str:
    try:
        repo_type = "Public" if repo.is_public else "Private"
        repo_tags = ", ".join(repo.topics) if repo.topics else "None"

        return "\n\n".join(
            ["<b>%s (%s)</b>" % (repo.name, repo_type,),
             "<b>%s</b>" % repo.description,
             "⭐️ <b>Stars:</b> %s" % repo.followers,
             "🤖 <b>Language:</b> %s" % repo.language,
             "🗓️ <b>Last update:</b> %s" % repo.last_updated,
             "#️⃣ <b>Tags:</b> %s" % repo_tags]
        )

    except Exception as exc:
        raise MakeMessageError(exc)


def remove_em_tag(data: str) -> str:
    return data.replace("<em>", "").replace("</em>", "")


def get_repo_reply_markup(repo_url: str):
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Open repository 👀",
                             url=repo_url)
    ]])


def search_github_repos(query) -> list[Repo] | None:
    url = "https://github.com/search?q=%s&type=repositories" % query

    response = requests.get(url)

    if response.status_code == 200:
        json_repos = response.json()["payload"]
        
        if json_repos.get("results", False):
            json_repos = json_repos["results"]
            repos: list[Repo] = list()

            for repo in json_repos:
                repo_name = remove_em_tag(repo["hl_name"])

                repos.append(
                    Repo(
                        archived=repo["archived"],
                        followers=repo["followers"],
                        name=repo_name,
                        description=remove_em_tag(
                            repo["hl_trunc_description"]) if repo["hl_trunc_description"] else None,
                        repo_id=repo["id"],
                        language=repo["language"],
                        is_public=repo["public"],
                        last_updated=repo["repo"]["repository"]["updated_at"],
                        sponsorable=repo["sponsorable"],
                        topics=repo["topics"],
                        url="https://github.com/" + repo_name
                    )
                )
            return repos
    return None
