#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
import sys


def top_ten(subreddit):
    """ Returns: top ten post titles
        or None if queried subreddit is invalid """
    headers = {'User-Agent': 'adedamolaCoal'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        posts = response.json().get('data')
        titles = posts.get('children')
        for title in titles:
            print(title.get('data').get('title'))
    else:
        print(None)