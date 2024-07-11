"""
Модуль для представления класса Circle с перегруженными операторами
"""

class Circle:
    """Класс для представления окружности"""

    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.get_circumference() > other.get_circumference()

    def __lt__(self, other):
        return self.get_circumference() < other.get_circumference()

    def __le__(self, other):
        return self.get_circumference() <= other.get_circumference()

    def __ge__(self, other):
        return self.get_circumference() >= other.get_circumference()

    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self

    def get_circumference(self):
        """Метод для получения длины окружности"""
        return 2 * 3.14159 * self.radius

    def __str__(self):
        return f"Circle with radius {self.radius}"


if __name__ == "__main__":
    circle1 = Circle(5)
    circle2 = Circle(10)
    print(circle1 == circle2)
    print(circle1 > circle2)
    print(circle1 < circle2)
    circle1 += 5
    print(circle1)
    circle2 -= 2
    print(circle2)
    circle3 = circle1 + 3
    print(circle3)
    circle4 = circle2 - 1
    print(circle4)
