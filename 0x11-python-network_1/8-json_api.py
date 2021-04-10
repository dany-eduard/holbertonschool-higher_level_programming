#!/usr/bin/python3
"""Sends a POST request."""
import requests
import sys

if __name__ == '__main__':
    """
    Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a paramete
    """
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    response = requests.post(url, data={"q": letter})
    try:
        res = response.json()
        if res:
            print("[{}] {}".format(res.get("id"), res.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
