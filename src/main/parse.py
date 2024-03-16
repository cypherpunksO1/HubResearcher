from bs4 import BeautifulSoup
import requests
import os

# URL страницы, откуда вы хотите получить содержимое метатега
url = 'https://github.com/Tishka17/deseos17'

# Отправляем GET-запрос на страницу
response = requests.get(url)

# Проверяем, что запрос был успешным
if response.status_code == 200:
    # Парсим HTML-контент страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ищем метатег с атрибутом og:image
    meta_tag = soup.find('meta', attrs={'property': 'og:image'})

    if meta_tag:
        image_url = meta_tag.get('content')
        print(image_url)

        # Отправляем GET-запрос на URL изображения
        image_response = requests.get(image_url)

        # Проверяем, что запрос был успешным
        if image_response.status_code == 200:
            # Получаем имя файла из URL
            file_name = image_url.split("/")[-1] + ".png"

            # Открываем файл для записи и записываем содержимое изображения
            with open(file_name, 'wb') as file:
                file.write(image_response.content)
            print(f'Изображение успешно сохранено как {file_name}')
        else:
            print('Ошибка при загрузке изображения.')
    else:
        print('Метатег og:image не найден.')
else:
    print('Ошибка при загрузке страницы.')
