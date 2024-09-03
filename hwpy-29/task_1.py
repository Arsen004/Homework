import mysql.connector
from mysql.connector import errorcode


def main():
    config = {
    'user': 'root',
    'password': 'root_password',
    'host': 'localhost'
    }

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        try:
            cursor.execute("CREATE DATABASE CompanyDB")
            print("База данных 'CompanyDB' создана.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                print("База данных уже существует.")
            else:
                print(f"Ошибка при создании базы данных: {err}")

        connection.database = 'CompanyDB'

        try:
            cursor.execute("CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'newpassword'")
            cursor.execute("GRANT ALL PRIVILEGES ON CompanyDB.* TO 'newuser'@'localhost'")
            cursor.execute("FLUSH PRIVILEGES")
            print("Пользователь 'newuser' создан и привилегии предоставлены.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_CANNOT_USER:
                print("Пользователь уже существует.")
            else:
                print(f"Ошибка при создании пользователя: {err}")

        try:
            cursor.execute("""
            CREATE TABLE Salary (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL
            )
            """)
            print("Таблица 'Salary' создана.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Таблица 'Salary' уже существует.")
            else:
                print(f"Ошибка при создании таблицы: {err}")

    except mysql.connector.Error as err:
        print(f"Ошибка подключения к MySQL: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Соединение с MySQL закрыто.")

if __name__ == "__main__":
    main()
