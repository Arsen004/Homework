"""
Программа на tkinter для получения данных с сайта jsonplaceholder по id и сохранения их в файл
"""

import tkinter as tk
from tkinter import messagebox
import requests
import json
import os

def fetch_data():
    """
    Делает запрос на сайт jsonplaceholder с указанным id и отображает данные.
    """
    id_value = id_entry.get()
    if not id_value.isdigit():
        messagebox.showerror("Ошибка", "ID должно быть числом")
        return

    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id_value}")
    if response.status_code == 200:
        data = response.json()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, json.dumps(data, indent=4))
    else:
        messagebox.showerror("Ошибка", "Не удалось получить данные")

def save_data():
    """
    Сохраняет полученные данные в файл.
    """
    data = result_text.get(1.0, tk.END).strip()
    if not data:
        messagebox.showerror("Ошибка", "Нет данных для сохранения")
        return

    if not os.path.exists("output"):
        os.makedirs("output")

    with open(f"output/data_{id_entry.get()}.json", "w") as file:
        file.write(data)
    messagebox.showinfo("Успех", "Данные успешно сохранены")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("JSON Placeholder Fetcher")

    tk.Label(root, text="Введите ID:").pack(pady=5)

    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)

    tk.Button(root, text="Получить данные", command=fetch_data).pack(pady=5)

    result_text = tk.Text(root, height=15, width=50)
    result_text.pack(pady=5)

    tk.Button(root, text="Сохранить данные", command=save_data).pack(pady=5)

    root.mainloop()
