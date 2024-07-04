"""
Модуль для представления классов устройств и их наследников
"""

class Device:
    """Класс для представления устройства"""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        """Метод для получения информации об устройстве"""
        return f"Brand: {self.brand}, Model: {self.model}"


class CoffeeMachine(Device):
    """Класс для представления кофемашины"""

    def __init__(self, brand, model, water_capacity):
        super().__init__(brand, model)
        self.water_capacity = water_capacity

    def make_coffee(self):
        """Метод для приготовления кофе"""
        return "Making coffee..."

    def get_info(self):
        """Метод для получения информации о кофемашине"""
        return f"{super().get_info()}, Water Capacity: {self.water_capacity}L"


class Blender(Device):
    """Класс для представления блендера"""

    def __init__(self, brand, model, power):
        super().__init__(brand, model)
        self.power = power

    def blend(self):
        """Метод для смешивания"""
        return "Blending..."

    def get_info(self):
        """Метод для получения информации о блендере"""
        return f"{super().get_info()}, Power: {self.power}W"


class MeatGrinder(Device):
    """Класс для представления мясорубки"""

    def __init__(self, brand, model, blade_material):
        super().__init__(brand, model)
        self.blade_material = blade_material

    def grind(self):
        """Метод для измельчения мяса"""
        return "Grinding meat..."

    def get_info(self):
        """Метод для получения информации о мясорубке"""
        return f"{super().get_info()}, Blade Material: {self.blade_material}"


if __name__ == "__main__":
    coffee_machine = CoffeeMachine("DeLonghi", "ECAM22.110", 1.8)
    print(coffee_machine.get_info())
    print(coffee_machine.make_coffee())

    blender = Blender("Philips", "HR3556", 700)
    print(blender.get_info())
    print(blender.blend())

    meat_grinder = MeatGrinder("Bosch", "MFW67440", "Stainless Steel")
    print(meat_grinder.get_info())
    print(meat_grinder.grind())
