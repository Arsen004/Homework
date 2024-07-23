"""
Этот модуль предоставляет функционал для создания файлов с рандомными числами
с использованием как последовательного, так и многопоточного подходов.
"""

import os
import random
import time
import threading

def create_file_with_random_number(filename):
    """
    Создает файл и записывает в него случайное число.

    Аргументы:
        filename (str): Имя создаваемого файла.
    """
    time.sleep(1)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(random.randint(1, 100)))

def main_sequential():
    """
    Выполняет создание файлов последовательно.
    """
    start_time = time.time()
    for i in range(1000):
        filename = f'file_{i}.txt'
        create_file_with_random_number(filename)
    end_time = time.time()
    print(f'Время выполнения последовательно: {end_time - start_time} секунд')

def main_multithreaded():
    """
    Выполняет создание файлов с использованием многопоточности.
    """
    start_time = time.time()
    threads = []
    
    for i in range(1000):
        filename = f'file_{i}.txt'
        thread = threading.Thread(target=create_file_with_random_number, args=(filename,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print(f'Время выполнения многопоточно: {end_time - start_time} секунд')

if __name__ == "__main__":
    main_multithreaded()
