import time

def create_file(file_name):
    """
    Создает файл с задержкой 1 секунду.

    """
    time.sleep(1)
    with open(file_name, 'w') as f:
        f.write('This is a test file.\n')

if __name__ == "__main__":
    for i in range(100):
        create_file(f'test_file_{i}.txt')
