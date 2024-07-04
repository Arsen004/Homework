"""
Модуль для представления классов кораблей и их наследников
"""

class Ship:
    """Класс для представления корабля"""

    def __init__(self, name, displacement):
        self.name = name
        self.displacement = displacement

    def get_info(self):
        """Метод для получения информации о корабле"""
        return f"Name: {self.name}, Displacement: {self.displacement} tons"


class Frigate(Ship):
    """Класс для представления фрегата"""

    def __init__(self, name, displacement, armament):
        super().__init__(name, displacement)
        self.armament = armament

    def get_info(self):
        """Метод для получения информации о фрегате"""
        return f"{super().get_info()}, Armament: {self.armament}"


class Destroyer(Ship):
    """Класс для представления эсминца"""

    def __init__(self, name, displacement, speed):
        super().__init__(name, displacement)
        self.speed = speed

    def get_info(self):
        """Метод для получения информации об эсминце"""
        return f"{super().get_info()}, Speed: {self.speed} knots"


class Cruiser(Ship):
    """Класс для представления крейсера"""

    def __init__(self, name, displacement, armor):
        super().__init__(name, displacement)
        self.armor = armor

    def get_info(self):
        """Метод для получения информации о крейсере"""
        return f"{super().get_info()}, Armor: {self.armor} mm"


if __name__ == "__main__":
    frigate = Frigate("Admiral Gorshkov", 4500, "Missiles")
    print(frigate.get_info())

    destroyer = Destroyer("USS Zumwalt", 15000, 30)
    print(destroyer.get_info())

    cruiser = Cruiser("Peter the Great", 25000, 150)
    print(cruiser.get_info())
