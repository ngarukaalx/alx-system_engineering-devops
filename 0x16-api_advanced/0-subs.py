#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    try:
        response = requests.get(url, allow_redirects=False)
        if response.status_code == 200:
            reddit_data = response.json()['data']
            subscribers_count = reddit_data['subreddit_subscribers']
            return subscribers_count
        else:
            return 0
    except Exception as e:
        print(f"error: {str(e)}")
        return 0
