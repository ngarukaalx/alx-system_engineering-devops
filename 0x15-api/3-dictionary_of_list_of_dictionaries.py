#!/usr/bin/python3
"""Returns a user information about his/her TODO list progress"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    """Only execute when run directly"""
    def employee_details(employee_id):
        """returns employee data as required"""

        base_url = "https://jsonplaceholder.typicode.com"
        user_url = f"{base_url}/users/{employee_id}"
        todo_url = f"{user_url}/todos"

        # fetch user info
        user_info = requests.get(user_url)
        user_data = user_info.json()

        # todo list for the user
        todos_info = requests.get(todo_url)
        todos_data = todos_info.json()

        # export data to json format
        return {employee_id: [
                {
                    "username": user_data['username'],
                    "task": todo['title'],
                    "completed": todo['completed']
                } for todo in todos_data
                ]}

    def all_employee():
        """return all employees todo in json format"""
        json_file = "todo_all_employees.json"

        # get all users id
        users_url = "https://jsonplaceholder.typicode.com/users"
        # fetch user data
        response = requests.get(users_url).json()
        # Extract user ids
        user_ids = [user['id'] for user in response]
        employees_data = {}

        for user_id in user_ids:
            employees_data.update(employee_details(user_id))

        # Export to json
        with open(json_file, "w", newline='') as json_file:
            json.dump(employees_data, json_file)
    # Call the function to generate the JSON file
    all_employee()
