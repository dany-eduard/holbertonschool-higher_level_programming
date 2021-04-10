#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
import urllib.request

if __name__ == "__main__":
    """
    Body response:
    - type: <class 'bytes'>
    - content: b'OK'
    - utf8 content: OK
    """
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8", "replace")))
