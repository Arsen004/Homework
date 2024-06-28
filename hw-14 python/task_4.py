"""
Модуль для представления классов с инкапсуляцией
"""

class MainClass:
    """Главный класс с текстовым полем"""

    def __init__(self, text=""):
        self.text = text

    def set_text(self, text=""):
        self.text = text

    def get_text(self):
        return self.text


class SubClass(MainClass):
    """Класс-потомок с дополнительным числовым полем"""

    def __init__(self, text="", number=0):
        super().__init__(text)
        self.number = number

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number


if __name__ == "__main__":
    MAIN_INSTANCE = MainClass("Привет")
    print(MAIN_INSTANCE.get_text())

    SUB_INSTANCE = SubClass("Привет", 42)
    print(SUB_INSTANCE.get_text())
    print(SUB_INSTANCE.get_number())
