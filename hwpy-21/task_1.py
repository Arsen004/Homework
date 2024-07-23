"""
Этот модуль предоставляет функционал для загрузки информации с 100 ссылок
с использованием как последовательного, так и асинхронного подходов.
"""
import requests
import asyncio
import time
import aiohttp


URLS = [
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/2',
] * 50

async def fetch(url, session):
    """
    Загружает информацию с заданного URL.

    Аргументы:
        url (str): URL для загрузки информации.
        session (aiohttp.ClientSession): Сессия для выполнения запроса.
    
    Возвращает:
        dict: Ответ в формате JSON.
    """
    async with session.get(url) as response:
        return await response.json()

async def fetch_all(urls):
    """
    Загружает информацию с нескольких URL асинхронно.

    Аргументы:
        urls (list): Список URL для загрузки информации.
    
    Возвращает:
        list: Список ответов в формате JSON.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        return await asyncio.gather(*tasks)

def main_sequential():
    """
    Выполняет загрузку информации с 100 URL последовательно.
    """
    start_time = time.time()
    for url in URLS:
        response = requests.get(url)
        data = response.json()
    end_time = time.time()
    print(f'Время выполнения последовательно: {end_time - start_time} секунд')

async def main_async():
    """
    Выполняет загрузку информации с 100 URL асинхронно.
    """
    start_time = time.time()
    await fetch_all(URLS)
    end_time = time.time()
    print(f'Время выполнения асинхронно: {end_time - start_time} секунд')

if __name__ == "__main__":

    asyncio.run(main_async())
