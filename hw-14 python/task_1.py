"""
Модуль для представления класса Автомобиль
"""

class Car:
    """Класс для представления автомобиля"""

    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_engine_volume(self, engine_volume):
        self.engine_volume = engine_volume

    def get_engine_volume(self):
        return self.engine_volume

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def display_info(self):
        """Вывод информации о машине"""
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Объем двигателя: {self.engine_volume} л")
        print(f"Цвет: {self.color}")
        print(f"Цена: {self.price} руб")


if __name__ == "__main__":
    CAR = Car("Model S", 2020, "Tesla", 2.5, "Красный", 5000000)
    CAR.display_info()
