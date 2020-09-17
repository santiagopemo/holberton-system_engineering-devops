#!/usr/bin/python3
"""Recurse it module"""
import requests
from sys import argv


def recurse(subreddit, hot_list=[]):
    """
    Recursive function that queries the Reddit API and returns a list
    containingthe titles of all hot articles for a given subreddit
    """
    if hot_list == []:
        after = "null"
    else:
        after = hot_list[-1].get('data').get("name")
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    headers = {"User-Agent": "santiagopemo"}
    response = requests.get(url, headers=headers, allow_redirects=False).json()
    hot_posts = response.get('data', {}).get('children', None)
    if hot_posts is None:
        return None
    else:
        for post in hot_posts:
            hot_list.append(post)
    if response.get('data').get('after') is None:
        return hot_list
    return recurse(subreddit, hot_list)
