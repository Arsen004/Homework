import json

from book import Book
from user import User

class Library:
    def __init__(self, user: User, book: Book):
        self.__user = user
        self.__book = book

    def read_from_file(self):
        with open(f"{__class__.__name__}.txt", "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except Exception as e:
                return None

    def write_to_file(self):
        with open(f"{__class__.__name__}.txt", "a+", encoding="utf-8") as file:
            json.dump({"user": self.__user.user, "book": self.__book.book}, file)


    def __str__(self):
        return f"Книгу -> {",".join(self.__book.book.values())}, взял: {"".join(self.__user.user.values())}."


    