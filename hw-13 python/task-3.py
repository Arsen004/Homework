'''Домашнее задание №13: Обработка исключений. Собственные
исключения'''
def access_array_element(arr, index):
    """Access the element at the given index in the array"""
    try:
        print(arr[index])
    except IndexError:
        print(f"Index {index} is out of range for the array.")


if __name__ == "__main__":
    ARR = [1, 2, 3, 4, 5]
    access_array_element(ARR, 2)
    access_array_element(ARR, 10)
