"""
Загрузка 10 рандомных картинок с сайта с использованием библиотеки aiohttp
и сохранение их в разные папки.
"""

import os
import aiohttp
import asyncio

URL = 'https://picsum.photos/200/300'
FOLDER_NAME = 'images_aiohttp'

async def download_image(session, url, folder_name, image_number):
    """
    Асинхронно загружает картинку по указанному URL и сохраняет в папку.

    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    async with session.get(url) as response:
        response.raise_for_status()
        content = await response.read()

        file_path = os.path.join(folder_name, f'image_{image_number}.jpg')
        with open(file_path, 'wb') as file:
            file.write(content)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, URL, FOLDER_NAME, i) for i in range(1, 11)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
