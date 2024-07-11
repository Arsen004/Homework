"""
Модуль для представления класса Roman с перегруженными операторами
"""

class Roman:
    """Класс для представления римского числа"""

    roman_to_int_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    int_to_roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        elif isinstance(value, str):
            self.value = self.roman_to_int(value)
        else:
            raise ValueError("Value must be an integer or a Roman numeral string")

    def __add__(self, other):
        return Roman(self.value + other.value)

    def __sub__(self, other):
        return Roman(self.value - other.value)

    def __mul__(self, other):
        return Roman(self.value * other.value)

    def __truediv__(self, other):
        return Roman(self.value // other.value)

    @staticmethod
    def roman_to_int(roman):
        """Метод для преобразования римского числа в целое"""
        total = 0
        prev_value = 0
        for char in reversed(roman):
            int_value = Roman.roman_to_int_map[char]
            if int_value < prev_value:
                total -= int_value
            else:
                total += int_value
            prev_value = int_value
        return total

    @staticmethod
    def int_to_roman(num):
        """Метод для преобразования целого числа в римское"""
        roman = ''
        for value, numeral in Roman.int_to_roman_map:
            while num >= value:
                roman += numeral
                num -= value
        return roman

    def __str__(self):
        return self.int_to_roman(self.value)


if __name__ == "__main__":
    num1 = Roman('X')
    num2 = Roman('V')
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
