#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID.
Returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import sys
    import requests
    import json

    url1 = "https://jsonplaceholder.typicode.com/todos/"
    response1 = requests.get(url1)
    data1 = response1.text
    list_data1 = json.loads(data1)
    completed = 0
    total = 0
    for task in list_data1:
        if task["userId"] == int(sys.argv[1]):
            total += 1
            if task["completed"]:
                completed += 1

    url2 = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    response2 = requests.get(url2)
    data2 = response2.text
    data2 = json.loads(data2)
    EMPLOYEE_NAME = data2["name"]

    print(f'Employee {EMPLOYEE_NAME} is done with tasks({completed}/{total})')
    for task in list_data1:
        if task["userId"] == int(sys.argv[1]) and task["completed"]:
            print(f'\t {task["title"]}')
