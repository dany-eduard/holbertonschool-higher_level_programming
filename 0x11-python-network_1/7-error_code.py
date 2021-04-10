#!/usr/bin/python3
"""Error codes."""
import requests
import sys

if __name__ == '__main__':
    """
    If the HTTP status code is greater than or equal to 400,
    print: Error code: followed by the value.
    """
    response = requests.get(sys.argv[1])
    if response.status_code < 400:
        print(response.text)
    else:
        print("Error code:", response.status_code)
