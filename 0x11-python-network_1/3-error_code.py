#!/usr/bin/python3
""" Error codes. """
import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    """
    Sends a request to the URL and displays the body of the
    response (decoded in utf-8). You have to manage
    urllib.error.HTTPError.
    """
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code:", error.code)
