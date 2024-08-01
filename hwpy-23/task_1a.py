"""
Загрузка 10 рандомных картинок с сайта с использованием библиотеки requests
и сохранение их в разные папки.
"""

import os
import requests

URL = 'https://picsum.photos/200/300'

FOLDER_NAME = 'images_requests'

def download_image(url, folder_name, image_number):
    """
    Загружает картинку по указанному URL и сохраняет в папку.

    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    response = requests.get(url)
    response.raise_for_status()

    file_path = os.path.join(folder_name, f'image_{image_number}.jpg')
    with open(file_path, 'wb') as file:
        file.write(response.content)

if __name__ == "__main__":
    for i in range(1, 11):
        download_image(URL, FOLDER_NAME, i)
