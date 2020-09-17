#!/usr/bin/python3
"""Count it module"""
import requests
from sys import argv


def count_words(subreddit, word_list):
    """
    Recursive function that queries the Reddit API, parses
    the title of all hot articles, and prints a sorted count
    of given keywords (case-insensitive, delimited by spaces
    """
    recurse = __import__('2-recurse').recurse
    try:
        hot_list = recurse(subreddit)
    except:
        return
    if hot_list is None:
        print()
        return
    words_dict = dict.fromkeys(word_list, 0)
    for post in hot_list:
        title = post.get('data').get('title').split()
        for word in word_list:
            for title_word in title:
                if word.lower() == title_word.lower():
                    words_dict[word] += 1
    sort_value = sorted(words_dict.items(), key=lambda i: i[::-1])
    sort_alpha = sorted(sort_value, key=lambda i: i[1], reverse=True)
    for word, value in sort_alpha:
        if value != 0:
            print('{}: {}'.format(word, value))
    return
