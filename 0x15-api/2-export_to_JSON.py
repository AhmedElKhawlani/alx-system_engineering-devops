#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID.
Exporst a json file about his/her TODO list progress.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    url1 = "https://jsonplaceholder.typicode.com/todos/"
    response1 = requests.get(url1)
    data1 = response1.text
    list_data1 = json.loads(data1)

    url2 = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    response2 = requests.get(url2)
    data2 = response2.text
    data2 = json.loads(data2)
    username = data2["username"]

    with open(sys.argv[1] + ".json", "w") as file:
        data = {sys.argv[1]: []}
        for task in list_data1:
            if task["userId"] == int(sys.argv[1]):
                data_task = {"task": task["title"],
                             "completed": task["completed"],
                             "username": username}
                data[sys.argv[1]].append(data_task)
        json.dump(data, file)
