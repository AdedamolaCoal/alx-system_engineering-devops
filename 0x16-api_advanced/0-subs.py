
#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
import sys


def number_of_subscribers(subreddit):
    """ subreddit: subreddit name
    Returns:
        number of subscribers to the subreddit,
        or 0 if subreddit request isn't valid"""
    headers = {'User-Agent': 'adedamolaCoal' }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        res = response.json().get("data")
        return res.get("subscribers")
    return (0) 