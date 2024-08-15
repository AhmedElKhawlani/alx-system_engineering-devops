#!/usr/bin/python3

"""
Module that defines a function,
that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed
    for a given subreddit
    """

    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Ahmed EL KHAWLANI"}
    response = requests.get(link, headers=headers, allow_redirects=False)
    if response.status_code in (404, 302):
        print("None")
        return
    data = response.json().get("data")
    counter = 0
    for c in data.get("children"):
        print(c.get("data").get("title"))
        counter += 1
        if counter == 10:
            break
