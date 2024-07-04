"""
Модуль для представления классов автомобиля с множественным наследованием
"""

class Wheels:
    """Класс для представления колес"""

    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    def get_wheels_info(self):
        """Метод для получения информации о колесах"""
        return f"Number of wheels: {self.number_of_wheels}"


class Engine:
    """Класс для представления двигателя"""

    def __init__(self, horsepower):
        self.horsepower = horsepower

    def get_engine_info(self):
        """Метод для получения информации о двигателе"""
        return f"Horsepower: {self.horsepower}"


class Doors:
    """Класс для представления дверей"""

    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors

    def get_doors_info(self):
        """Метод для получения информации о дверях"""
        return f"Number of doors: {self.number_of_doors}"


class Car(Wheels, Engine, Doors):
    """Класс для представления автомобиля"""

    def __init__(self, number_of_wheels, horsepower, number_of_doors):
        Wheels.__init__(self, number_of_wheels)
        Engine.__init__(self, horsepower)
        Doors.__init__(self, number_of_doors)

    def get_info(self):
        """Метод для получения информации об автомобиле"""
        return f"{self.get_wheels_info()}, {self.get_engine_info()}, {self.get_doors_info()}"


if __name__ == "__main__":
    car = Car(4, 300, 4)
    print(car.get_info())
