#!/usr/bin/python3
""" Sends a POST request. """
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    """
    Script that takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8).
    """
    email = urllib.parse.urlencode({"email": sys.argv[2]}).encode()
    with urllib.request.urlopen(sys.argv[1], email) as response:
        print(response.read().decode('utf-8'))
