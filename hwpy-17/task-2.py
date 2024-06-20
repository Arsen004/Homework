'''Домашнее задание №11: Работа с комплексными файлами - excel, json,
word. Git и Jira'''
import json
import requests
import os

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/todos/'
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()
        with open('todos.json', 'w') as file:
            json.dump(todos, file, indent=4)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

    # Step b: Read the JSON file into a Python list of dictionaries
    with open('todos.json', 'r') as file:
        todos = json.load(file)

    # Step c: Write each dictionary to a separate JSON file
    if not os.path.exists('todos'):
        os.makedirs('todos')

    for i, todo in enumerate(todos):
        with open(f'todos/todo_{i+1}.json', 'w') as file:
            json.dump(todo, file, indent=4)

    print("All tasks have been written to separate JSON files.")
