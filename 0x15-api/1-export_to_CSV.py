#!/usr/bin/python3
"""Returns a user information about his/her TODO list progress"""

import csv
import requests
import sys

if __name__ == "__main__":
    """Only execute when run directly"""
    employee_id = sys.argv[1]
    csv_file = "USER_ID.csv"

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

        # create CSV file
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for todo in todos_data:
                writer.writerow(
                        [employee_id, user_data['name'],
                            todo['completed'], todo['title']])
