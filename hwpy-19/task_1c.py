import time
import threading

def create_file(file_name):
    """
    Создает файл с задержкой 1 секунду.
    
    """
    time.sleep(1)
    with open(file_name, 'w') as f:
        f.write('This is a test file.\n')

if __name__ == "__main__":
    start_time = time.time()
    
    threads = []
    for i in range(100):
        thread = threading.Thread(target=create_file, args=(f'test_file_{i}.txt',))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print(f"Время выполнения с многопоточностью: {end_time - start_time} секунд")
