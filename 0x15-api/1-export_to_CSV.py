#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the CSV format
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    api_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users/{}'.format(api_url, employee_id)
    todos_user_url = '{}/todos?userId={}'.format(api_url, employee_id)
    r_employee = requests.get(user_url).json()
    r_todos_employee = requests.get(todos_user_url).json()
    filename = '{}.csv'.format(employee_id)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in r_todos_employee:
            writer.writerow([employee_id, r_employee.get("username"),
                            task.get("completed"), task.get("title")])
