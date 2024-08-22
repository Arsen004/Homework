'''Домашка'''
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt6.QtCore import Qt
import requests
import json
import os

class JsonPlaceholderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle('JSONPlaceholder Client')
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        self.id_label = QLabel('Введите ID:')
        layout.addWidget(self.id_label)

        self.id_input = QLineEdit()
        layout.addWidget(self.id_input)

        self.request_button = QPushButton('Отправить запрос')
        layout.addWidget(self.request_button)
        self.request_button.clicked.connect(self.make_request)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.save_button = QPushButton('Сохранить результат')
        layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.save_result)

        self.setLayout(layout)

    def make_request(self):

        post_id = self.id_input.text()
        url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            formatted_json = json.dumps(data, indent=4)
            self.result_text.setText(formatted_json)
        else:
            self.result_text.setText(f'Ошибка: {response.status_code}')

    def save_result(self):

        data = self.result_text.toPlainText()

        if data:
            save_dir = 'json_results'
            os.makedirs(save_dir, exist_ok=True)
            post_id = self.id_input.text()
            file_path = os.path.join(save_dir, f'post_{post_id}.json')

            with open(file_path, 'w') as file:
                file.write(data)
            self.result_text.append(f'\nРезультат сохранен в {file_path}')
        else:
            self.result_text.setText('Нет данных для сохранения.')

if __name__ == '__main__':
    app = QApplication([])
    window = JsonPlaceholderApp()
    window.show()
    app.exec()
