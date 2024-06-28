"""
Модуль для представления класса Книга
"""

class Book:
    """Класс для представления книги"""

    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def display_info(self):
        """Вывод информации о книге"""
        print(f"Название: {self.title}")
        print(f"Год выпуска: {self.year}")
        print(f"Издатель: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Цена: {self.price} руб")


if __name__ == "__main__":
    BOOK = Book("Война и мир", 1869, "АСТ", "Роман", "Л.Н. Толстой", 1500)
    BOOK.display_info()
