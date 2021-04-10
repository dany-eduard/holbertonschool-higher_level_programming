#!/usr/bin/python3
"""Github challenge."""
import requests
import sys

if __name__ == "__main__":
    """
    Please list 10 commits (from the most recent to oldest).
    """
    url = "https://api.github.com/repos/{}/{}/commits"\
        .format(sys.argv[2], sys.argv[1])
    r = (requests.get(url).json())[:10]
    for num in r:
        print("{}: {}".format(num['sha'], num['commit']['author']['name']))
