"""
Этот модуль загружает массив JSON-объектов с сайта jsonplaceholder,
используя библиотеку aiohttp, и сохраняет каждый объект в отдельный файл.
"""

import os
import json
import aiohttp
import asyncio


URL = 'https://jsonplaceholder.typicode.com/todos'
FOLDER_NAME = 'json_files_aiohttp'

async def fetch_data(session, url):
    """
    Асинхронно загружает данные с указанного URL.

    Аргументы:
        session (aiohttp.ClientSession): Сессия для выполнения запроса.
        url (str): URL для загрузки данных.
    
    Возвращает:
        list: Список данных в формате JSON.
    """
    async with session.get(url) as response:
        return await response.json()

async def save_to_files(data, folder_name):
    """
    Сохраняет данные в отдельные файлы.

    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for i, item in enumerate(data):
        file_path = os.path.join(folder_name, f'item_{i+1}.json')
        with open(file_path, 'w') as file:
            json.dump(item, file, indent=4)

async def main():
    """
    Основная асинхронная функция для загрузки и сохранения данных.
    """
    async with aiohttp.ClientSession() as session:
        data = await fetch_data(session, URL)
        await save_to_files(data, FOLDER_NAME)

if __name__ == "__main__":
    asyncio.run(main())
