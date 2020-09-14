#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    api_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users/{}'.format(api_url, employee_id)
    todos_user_url = '{}/todos?userId={}'.format(api_url, employee_id)
    r_employee = requests.get(user_url).json()
    r_todos_employee = requests.get(todos_user_url).json()
    done_tasks = []
    for task in r_todos_employee:
        if task.get("completed") is True:
            done_tasks.append(task)
    print('Employee {} is done with tasks({}/{}):'.format(
            r_employee.get("name"), len(done_tasks), len(r_todos_employee)))
    for done_task in done_tasks:
        print('\t {}'.format(done_task.get("title")))
