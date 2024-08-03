"""
Программа на tkinter для получения данных с сайта jsonplaceholder по id и сохранения их в файл
"""

import tkinter as tk
from tkinter import messagebox
import requests
import json
import os

class JsonPlaceholderFetcher:
    """
    Класс для создания интерфейса программы с использованием tkinter.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("JSON Placeholder Fetcher")
        
        self.create_widgets()

    def create_widgets(self):
        """
        Создаёт виджеты в главном окне.
        """
        self.label = tk.Label(self.root, text="Введите ID:")
        self.label.pack(pady=5)
        
        self.id_entry = tk.Entry(self.root)
        self.id_entry.pack(pady=5)
        
        self.fetch_button = tk.Button(self.root, text="Получить данные", command=self.fetch_data)
        self.fetch_button.pack(pady=5)
        
        self.result_text = tk.Text(self.root, height=15, width=50)
        self.result_text.pack(pady=5)
        
        self.save_button = tk.Button(self.root, text="Сохранить данные", command=self.save_data)
        self.save_button.pack(pady=5)
    
    def fetch_data(self):
        """
        Делает запрос на сайт jsonplaceholder с указанным id и отображает данные.
        """
        id_value = self.id_entry.get()
        if not id_value.isdigit():
            messagebox.showerror("Ошибка", "ID должно быть числом")
            return

        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id_value}")
        if response.status_code == 200:
            data = response.json()
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, json.dumps(data, indent=4))
        else:
            messagebox.showerror("Ошибка", "Не удалось получить данные")

    def save_data(self):
        """
        Сохраняет полученные данные в файл.
        """
        data = self.result_text.get(1.0, tk.END).strip()
        if not data:
            messagebox.showerror("Ошибка", "Нет данных для сохранения")
            return

        if not os.path.exists("output"):
            os.makedirs("output")

        with open(f"output/data_{self.id_entry.get()}.json", "w") as file:
            file.write(data)
        messagebox.showinfo("Успех", "Данные успешно сохранены")

if __name__ == "__main__":
    root = tk.Tk()
    app = JsonPlaceholderFetcher(root)
    root.mainloop()
