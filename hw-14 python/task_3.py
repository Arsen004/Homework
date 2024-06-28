"""
Модуль для представления класса Стадион
"""

class Stadium:
    """Класс для представления стадиона"""

    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_opening_date(self, opening_date):
        self.opening_date = opening_date

    def get_opening_date(self):
        return self.opening_date

    def set_country(self, country):
        self.country = country

    def get_country(self):
        return self.country

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_capacity(self):
        return self.capacity

    def display_info(self):
        """Вывод информации о стадионе"""
        print(f"Название: {self.name}")
        print(f"Дата открытия: {self.opening_date}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Вместимость: {self.capacity} зрителей")


if __name__ == "__main__":
    STADIUM = Stadium("Лужники", "1956-07-31", "Россия", "Москва", 81000)
    STADIUM.display_info()
