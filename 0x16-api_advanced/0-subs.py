#!/usr/bin/python3

"""
Module that defines a function,
that queries the Reddit API and returns the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers.
    """

    if (not subreddit) or (type(subreddit) is not str):
        return 0
    link = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "Ahmed EL KHAWLANI"}
    response = requests.get(link, headers=headers, allow_redirects=False)
    if response.status_code == 302:
        return 0
    data = response.json()
    subs = data.get("data", {}).get("subscribers", 0)
    return subs
