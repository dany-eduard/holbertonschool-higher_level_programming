#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    """
    Body response:
        - type: <class 'bytes'>
        - content: b'OK'
        - utf8 content: OK
    """
    status = response.read()
    print('Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'
        .format(type(status), status, status.decode('utf-8')))
