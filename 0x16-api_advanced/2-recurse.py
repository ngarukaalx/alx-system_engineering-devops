#!/usr/bin/python3
"""
recursive calls in API
"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """make recursives calls"""

    global after

    params = {'after': after}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(url, params=params, allow_redirects=False)

    if response.status_code == 200:
        pagination = response.json()["data"].get("after")
        if pagination is not None:
            after = pagination
            recurse(subreddit, hot_list)
        titles = response.json()["data"].get("children")
        for title in titles:
            hot_list.append(title.get("data").get("title"))
        return hot_list
    else:
        return (None)
