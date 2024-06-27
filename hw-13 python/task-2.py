'''Домашнее задание №13: Обработка исключений. Собственные
исключения'''
def plus_two(number):
    """Add 2 to the given number and print the result"""
    try:
        result = number + 2
        print(result)
    except TypeError:
        print("Ожидаемый тип данных — число!")


if __name__ == "__main__":
    plus_two(5)
    plus_two("5")
