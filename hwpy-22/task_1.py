"""
Этот модуль загружает массив JSON-объектов с сайта jsonplaceholder,
используя библиотеку requests, и сохраняет каждый объект в отдельный файл.
"""

import os
import requests
import json


URL = 'https://jsonplaceholder.typicode.com/todos'

FOLDER_NAME = 'json_files_requests'

def fetch_data(url):
    """
    Загружает данные с указанного URL.

    Аргументы:
        url (str): URL для загрузки данных.
    
    Возвращает:
        list: Список данных в формате JSON.
    """
    response = requests.get(url)
    response.raise_for_status()  
    return response.json()

def save_to_files(data, folder_name):
    """
    Сохраняет данные в отдельные файлы.

    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for i, item in enumerate(data):
        file_path = os.path.join(folder_name, f'item_{i+1}.json')
        with open(file_path, 'w') as file:
            json.dump(item, file, indent=4)

if __name__ == "__main__":
    data = fetch_data(URL)
    save_to_files(data, FOLDER_NAME)
