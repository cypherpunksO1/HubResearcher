from bs4 import BeautifulSoup
import requests
import os

from src.parsers.exceptions import *


def save_repo_image(repo_url: str):
    response = requests.get(repo_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        meta_tag = soup.find('meta', attrs={'property': 'og:image'})

        if meta_tag:
            image_url = meta_tag.get('content')

            image_response = requests.get(image_url)

            if image_response.status_code == 200:
                file_name = image_url.split("/")[-1] + ".png"
                
                with open(file_name, 'wb') as file:
                    file.write(image_response.content)
                return True
            else:
                raise ImageDownloadError()
        else:
            raise OgMetaTagNotFound()
    else:
        raise PageLoadError()