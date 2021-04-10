#!/usr/bin/python3
"""Script for response header value."""
import urllib.request
import sys

if __name__ == "__main__":
    """
    Sends a request to the URL and displays
    the value of the X-Request-Id variable
    found in the header of the response.
    """
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
