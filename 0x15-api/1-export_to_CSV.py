#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID.
Returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import csv
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
    n = data2["username"]

    with open(sys.argv[1] + ".csv", "w") as file:
        csv_file = csv.writer(file)
        lines = []
        for task in list_data1:
            if task["userId"] == int(sys.argv[1]):
                line = [sys.argv[1], n, str(task["completed"]), task["title"]]
                lines.append(line)
        csv_file.writerows(lines)
