"""
Модуль для представления классов с инкапсуляцией
"""

class MainClass:
    """Главный класс с текстовым полем"""

    def __init__(self, name=""):
        self.name = name

    def set_name(self, name=""):
        """Метод для присваивания значения текстовому полю"""
        self.name = name

    def get_name(self):
        """Метод для получения значения текстового поля"""
        return self.name


class SubClass(MainClass):
    """Класс-потомок с дополнительным числовым полем"""

    def __init__(self, name="", age=0):
        super().__init__(name)
        self.age = age

    def set_age(self, age):
        """Метод для присваивания значения числовому полю"""
        self.age = age

    def get_age(self):
        """Метод для получения значения числового поля"""
        return self.age


if __name__ == "__main__":
    MAIN_INSTANCE = MainClass("Мария")
    print(MAIN_INSTANCE.get_name())

    MAIN_INSTANCE.set_name("Саша")
    print(MAIN_INSTANCE.get_name())

    SUB_INSTANCE = SubClass("Мария", 24)
    print(SUB_INSTANCE.get_name())
    print(SUB_INSTANCE.get_age())

    SUB_INSTANCE.set_name("Леша")
    SUB_INSTANCE.set_age(17)
    print(SUB_INSTANCE.get_name())
    print(SUB_INSTANCE.get_age())
