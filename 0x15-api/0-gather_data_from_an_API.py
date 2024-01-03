#!/usr/bin/python3
"""Returns a user information about his/her TODO list progress"""

import requests
import sys

if __name__ == "__main__":
    """Only execute when run directly"""
    employee_id = sys.argv[1]

    if employee_id.isdigit():
        base_url = "https://jsonplaceholder.typicode.com"
        user_url = f"{base_url}/users/{employee_id}"
        todo_url = f"{user_url}/todos"

        # fetch user info
        user_info = requests.get(user_url)
        user_data = user_info.json()

        # todo list for the user
        todos_info = requests.get(todo_url)
        todos_data = todos_info.json()
        # calculate completed tasks
        complete_tasks = [todo for todo in todos_data if todo["completed"]]
        total_tasks = len(todos_data)
        print(f"Employee {user_data['name']} is done with tasks"
              f"({len(complete_tasks)}/{total_tasks}):")
        for task in complete_tasks:
            print(f"\t {task['title']}")
