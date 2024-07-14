"""
Приложение для создания Word-файла с текстом, введенным пользователем.
"""

from docx import Document

def main():
    """Главная функция для получения текста и создания Word-файла."""
    user_text = input("Введите текст для сохранения в Word-файл: ")

    doc = Document()
    doc.add_paragraph(user_text)
    doc.save('output.docx')

    print("Файл output.docx успешно создан.")

if __name__ == "__main__":
    main()
