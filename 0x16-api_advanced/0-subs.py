#!/usr/bin/python3
"""How many subscribers module"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns
    the number of subscribers for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "santiagopemo"}
    response = requests.get(url, headers=headers).json()
    subscribers = response.get('data', {}).get('subscribers', 0)
    return subscribers
