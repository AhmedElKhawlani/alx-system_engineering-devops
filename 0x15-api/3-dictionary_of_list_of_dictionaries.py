#!/usr/bin/python3
"""
Python script that, using this REST API.
Export a json file about all Users TODO list progress.
"""

if __name__ == "__main__":
    import json
    import requests

    url1 = "https://jsonplaceholder.typicode.com/todos/"
    response1 = requests.get(url1)
    data1 = response1.text
    list_data1 = json.loads(data1)

    def getUsername(Id):
        url2 = "https://jsonplaceholder.typicode.com/users/" + str(Id)
        response2 = requests.get(url2)
        data2 = response2.text
        data2 = json.loads(data2)
        username = data2["username"]
        return username

    with open("todo_all_employees.json", "w") as file:
        data = {}
        for task in list_data1:
            userId = task["userId"]
            username = getUsername(userId)
            data_task = {"username": username,
                         "task": task["title"],
                         "completed": task["completed"]}
            if userId in data:
                data[userId].append(data_task)
            else:
                data[userId] = [data_task]
        json.dump(data, file)
