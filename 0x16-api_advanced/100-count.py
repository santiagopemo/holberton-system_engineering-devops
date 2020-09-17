#!/usr/bin/python3
"""Count it module"""
import requests
from sys import argv


def count_words(subreddit, word_list, hot_list=[]):
    """
    Recursive function that queries the Reddit API, parses
    the title of all hot articles, and prints a sorted count
    of given keywords (case-insensitive, delimited by spaces
    """
    if hot_list == []:
        after = "null"
    else:
        after = hot_list[-1].get('data').get("name")
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    headers = {"User-Agent": "santiagopemo"}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False).json()
    except:
        print()
        return
    hot_posts = response.get('data', {}).get('children', None)
    if hot_posts is None:
        print()
        return
    else:
        hot_list.extend(hot_posts)
    if response.get('data').get('after') is None:
        words_dict = dict.fromkeys(word_list, 0)
        for post in hot_list:
            title = post.get('data').get('title').split()
            for word in word_list:
                for title_word in title:
                    if word.lower() == title_word.lower():
                        words_dict[word] += 1
        for word, value in sorted(words_dict.items(), key=lambda i: i[1],
                                  reverse=True):
            if value != 0:
                print('{}: {}'.format(word, value))
        return
    return count_words(subreddit, word_list, hot_list)
