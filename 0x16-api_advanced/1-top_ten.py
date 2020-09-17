#!/usr/bin/python3
"""Top ten module"""
import requests
from sys import argv


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {"User-Agent": "santiagopemo"}
    response = requests.get(url, headers=headers, allow_redirects=False).json()
    hot_posts = response.get('data', {}).get('children', None)
    if hot_posts is None:
        print("None")
    else:
        for post in hot_posts:
            print(post.get('data').get('title'))
