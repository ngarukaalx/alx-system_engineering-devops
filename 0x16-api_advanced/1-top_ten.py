#!/usr/bin/python3
"""titles of the first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """titles of the first 10 hot posts listed for a given subreddit"""

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    try:
        response = requests.get(url, allow_redirects=False)
        if response.status_code == 200:
            reddit_data = response.json()['data']
            print(reddit_data)
            return post_count
        else:
            return None
    except Exception as e:
        print(f"error: {str(e)}")
        return None
