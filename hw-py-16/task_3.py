"""
Модуль для представления классов с множественным наследованием
"""

class Square:
    """Класс для представления квадрата"""

    def __init__(self, side_length):
        self.side_length = side_length


class Circle:
    """Класс для представления окружности"""

    def __init__(self, radius):
        self.radius = radius


class InscribedCircle(Square, Circle):
    """Класс для представления окружности, вписанной в квадрат"""

    def __init__(self, side_length):
        Square.__init__(self, side_length)
        Circle.__init__(self, side_length / 2)


if __name__ == "__main__":
    inscribed_circle = InscribedCircle(10)
    print(f"Side length of the square: {inscribed_circle.side_length}")
    print(f"Radius of the inscribed circle: {inscribed_circle.radius}")
