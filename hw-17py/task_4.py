"""
Модуль для представления класса Flat с перегруженными операторами
"""

class Flat:
    """Класс для представления квартиры"""

    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __str__(self):
        return f"Flat area: {self.area} sqm, Price: {self.price} USD"


if __name__ == "__main__":
    flat1 = Flat(70, 50000)
    flat2 = Flat(80, 60000)
    print(flat1 == flat2)
    print(flat1 != flat2)
    print(flat1 > flat2)
    print(flat1 < flat2)
    print(flat1 <= flat2)
    print(flat1 >= flat2)
