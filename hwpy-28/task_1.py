import psycopg2
from psycopg2 import sql

def get_connection():
    try:
        connection = psycopg2.connect(
            dbname="your_db_name",  
            user="your_user",       
            password="your_password",  
            host="localhost"       
        )
        return connection
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

def read_all_rows():
    connection = get_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM students;")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
        except Exception as e:
            print(f"Ошибка при чтении всех строк: {e}")
        finally:
            connection.close()

def read_one_row(student_id):
    connection = get_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM students WHERE id = %s;", (student_id,))
                row = cursor.fetchone()
                print(row)
        except Exception as e:
            print(f"Ошибка при чтении строки: {e}")
        finally:
            connection.close()


def create_student(name, age, grade):
    connection = get_connection()
    if connection:
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s) RETURNING id;",
                                   (name, age, grade))
                    new_id = cursor.fetchone()[0]
                    print(f"Новый студент добавлен с ID: {new_id}")
        except Exception as e:
            print(f"Ошибка при добавлении студента: {e}")
        finally:
            connection.close()

def update_student(student_id, name, age, grade):
    connection = get_connection()
    if connection:
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s;",
                                   (name, age, grade, student_id))
                    print(f"Студент с ID {student_id} обновлен.")
        except Exception as e:
            print(f"Ошибка при обновлении студента: {e}")
        finally:
            connection.close()

def delete_student(student_id):
    connection = get_connection()
    if connection:
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM students WHERE id = %s;", (student_id,))
                    print(f"Студент с ID {student_id} удален.")
        except Exception as e:
            print(f"Ошибка при удалении студента: {e}")
        finally:
            connection.close()

if __name__ == "__main__":

    create_student("Иван Иванов", 20, "A")
    read_all_rows()
    read_one_row(1)
    update_student(1, "Петр Петров", 21, "B")
    delete_student(1)
