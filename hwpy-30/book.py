class Book:
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author

    @property
    def book(self):
        return {"author": self.__author, "title": self.__title}

    @book.setter
    def book(self, title: str, author: str):
        self.__title = title
        self.__author = author

    def __str__(self):
        return f"Автор: {self.__author} - Название книги: {self.__title}"
