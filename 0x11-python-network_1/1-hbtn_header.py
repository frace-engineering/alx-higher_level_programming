#!/usr/bin/python3
""" Python script that takes in a url, send a request to the url and
    displays the value of the x-Request-Id variable found in the
    header of the response
    """
import urllib.request
import sys


if __name__ == "__main__":
    """Pass url in the cli and request for the x-request-id """
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        request_id = response.getheader('X-Request-Id')
        print(request_id)
