#!/usr/bin/python3
"""Connect to Github api."""
import requests
import sys

if __name__ == '__main__':
    """
    Script that takes your GitHub credentials and uses
    the GitHub API to display your id.
    """
    url = 'https://api.github.com/user'
    res = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    try:
        print(res.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
