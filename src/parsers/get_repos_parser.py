


import requests
import pprint
from bs4 import BeautifulSoup
from dataclasses import dataclass

from src.parsers.exceptions import *


@dataclass
class Repo:
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
        repo_tags = ", ".join(repo.topics)
        
        return ("<b>%s (%s)</b>\n\n"\
                "<b>%s</b>\n\n"\
                "<b>Followers:</b> %s\n"\
                "<b>Language:</b> %s\n"\
                "<b>Last update:</b> %s\n"\
                "<b>Tags:</b> %s") % (
                    repo.name, repo_type, 
                    repo.description, 
                    repo.followers, 
                    repo.language, 
                    repo.last_updated, 
                    repo_tags
                )
    except Exception:
        raise MakeMessageError()


def search_github_repos(query) -> list[Repo] | None:
    url = "https://github.com/search?q=%s&type=repositories" % query

    response = requests.get(url)

    if response.status_code == 200:
        json_repos = response.json()["payload"]["results"]
        repos: list[Repo] = list()

        for repo in json_repos:
            repos.append(
                Repo(
                    archived=repo["archived"],
                    followers=repo["followers"],
                    name=repo["hl_name"],
                    description=repo["hl_trunc_description"],
                    repo_id=repo["id"],
                    language=repo["language"],
                    is_public=repo["public"],
                    last_updated=repo["repo"]["repository"]["updated_at"],
                    sponsorable=repo["sponsorable"],
                    topics=repo["topics"],
                )
            )
        return repos
    return None
