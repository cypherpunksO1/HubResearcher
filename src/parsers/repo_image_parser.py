from bs4 import BeautifulSoup
import requests
import os

from src.parsers.exceptions import *


def save_repo_image(repo_name: str, return_only_og: bool = False):
    url = "https://github.com/%s" % repo_name
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        meta_tag = soup.find('meta', attrs={'property': 'og:image'})

        if meta_tag:
            image_url = meta_tag.get('content')
            
            if return_only_og:
                return image_url

            image_response = requests.get(image_url)

            if image_response.status_code == 200:
                save_path = os.getenv("DEFAULT_IMAGES_DIR")
                
                repo_owner = repo_name.split("/")[0]
                
                try:
                    os.mkdir(save_path + repo_owner)
                except FileExistsError:
                    pass
                
                file_name = save_path + repo_name + ".png"
                
                with open(file_name, 'wb') as file:
                    file.write(image_response.content)
                return True
            else:
                raise ImageDownloadError()
        else:
            raise OgMetaTagNotFound()
    else:
        raise PageLoadError()