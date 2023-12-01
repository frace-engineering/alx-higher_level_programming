#!/usr/bin/python3
""" Python script that takes in a url and an email, send a request to
    the url with the email as a parameter and displays the body of the
    response (decoded in utf-8)
    """
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    """Pass url and the email in the cli and print the response """
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    param = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(url, param)
    with urllib.request.urlopen(req) as response:
        page_content = response.read().decode('utf-8')
    print(f'{page_content}')
