from book import Book
from user import User
from library import Library

def main() -> None:
    # Точка входа программы
    # Создаем книги
    book1 = Book("1984", "George Orwell")
    book2 = Book("Brave New World", "Aldous Huxley")
    # Создаем пользователей
    user1 = User("Alice")
    user2 = User("Bob")

    # Выводим информацию о книгах и пользователях
    print(book1)
    print(book2)
    print(user1)
    print(user2)

    library1 = Library(user1, book1)
    library2 = Library(user2, book2)
    print(library1)
    print(library2)

    library1.write_to_file()
    print(library1.read_from_file())

if __name__ == "__main__":
    main()