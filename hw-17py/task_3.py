"""
Модуль для представления класса Airplane с перегруженными операторами
"""

class Airplane:
    """Класс для представления самолета"""

    def __init__(self, model, passenger_capacity):
        self.model = model
        self.passenger_capacity = passenger_capacity
        self.passengers_onboard = 0

    def __eq__(self, other):
        return self.model == other.model

    def __gt__(self, other):
        return self.passenger_capacity > other.passenger_capacity

    def __lt__(self, other):
        return self.passenger_capacity < other.passenger_capacity

    def __le__(self, other):
        return self.passenger_capacity <= other.passenger_capacity

    def __ge__(self, other):
        return self.passenger_capacity >= other.passenger_capacity

    def __add__(self, passengers):
        self.passengers_onboard += passengers
        return self

    def __sub__(self, passengers):
        self.passengers_onboard -= passengers
        return self

    def __iadd__(self, passengers):
        self.passengers_onboard += passengers
        return self

    def __isub__(self, passengers):
        self.passengers_onboard -= passengers
        return self

    def __str__(self):
        return (f"Airplane model: {self.model}, Capacity: {self.passenger_capacity}, "
                f"Passengers onboard: {self.passengers_onboard}")


if __name__ == "__main__":
    plane1 = Airplane("Boeing 737", 150)
    plane2 = Airplane("Airbus A320", 180)
    print(plane1 == plane2)
    print(plane1 > plane2)
    print(plane1 < plane2)
    plane1 += 20
    print(plane1)
    plane2 -= 10
    print(plane2)
    plane1 + 50
    print(plane1)
    plane2 - 20
    print(plane2)
