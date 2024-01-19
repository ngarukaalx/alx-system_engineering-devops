#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 404:
        return 0
    if response.status_code == 200:
        # converts response into python dict Extracts data
        reddit_data = response.json().get("data")

        # returns subscribers
        return reddit_data.get("subscribers")
    else:
        return 0
