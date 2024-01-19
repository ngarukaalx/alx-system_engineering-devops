#!/usr/bin/python3
"""titles of the first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """titles of the first 10 hot posts listed for a given subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(url, allow_redirects=False)
    if response.status_code == 404:
        print("None")
    if response.status_code == 200:
        reddit_data = response.json()['data']
        hot_post = reddit_data.get("children")[:10]
        for post in hot_post:
            title = post['data'].get("title")
            print(title)
    else:
        print("None")
