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
    link = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(link).json()
    subs = req.get("data", {}).get("subscribers", 0)
    return subs
