"""
Модуль для представления классов фигур и их операций
"""

import json

class Shape:
    """Базовый класс для представления плоских фигур"""

    def __init__(self, name):
        self.name = name

    def show(self):
        """Метод для вывода информации о фигуре"""
        print(f"Shape: {self.name}")

    def save(self, filename):
        """Метод для сохранения фигуры в файл"""
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(self.__dict__, file)

    @classmethod
    def load(cls, filename):
        """Метод для считывания фигуры из файла"""
        with open(filename, 'r', encoding="utf-8") as file:
            data = json.load(file)
            shape = cls(data['name'])
            shape.__dict__.update(data)
            return shape


class Square(Shape):
    """Класс для представления квадрата"""

    def __init__(self, name, x, y, side_length):
        super().__init__(name)
        self.x = x
        self.y = y
        self.side_length = side_length

    def show(self):
        """Метод для вывода информации о квадрате"""
        super().show()
        print(f"Square at ({self.x}, {self.y}) with side length {self.side_length}")


class Rectangle(Shape):
    """Класс для представления прямоугольника"""

    def __init__(self, name, x, y, width, height):
        super().__init__(name)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        """Метод для вывода информации о прямоугольнике"""
        super().show()
        print(f"Rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}")


class Circle(Shape):
    """Класс для представления окружности"""

    def __init__(self, name, x, y, radius):
        super().__init__(name)
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        """Метод для вывода информации об окружности"""
        super().show()
        print(f"Circle at ({self.x}, {self.y}) with radius {self.radius}")


class Ellipse(Shape):
    """Класс для представления эллипса"""

    def __init__(self, name, x, y, width, height):
        super().__init__(name)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        """Метод для вывода информации об эллипсе"""
        super().show()
        print(f"Ellipse at ({self.x}, {self.y}) with width {self.width} and height {self.height}")


if __name__ == "__main__":
    shapes = [
        Square("Square1", 0, 0, 10),
        Rectangle("Rectangle1", 10, 10, 20, 15),
        Circle("Circle1", 5, 5, 7),
        Ellipse("Ellipse1", 2, 2, 15, 10)
    ]

    for shape in shapes:
        shape.show()
        shape.save(f"{shape.name}.json")

    loaded_shapes = [Shape.load(f"{shape.name}.json") for shape in shapes]

    for shape in loaded_shapes:
        shape.show()
