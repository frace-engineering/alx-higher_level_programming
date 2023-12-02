#!/usr/bin/python3
""" Python script that takes in a url, sends a request
    to the url and displays the body of the request
    """

import requests
import sys


if __namae__ == "__main__":
    """ Request and raise exception as error occures """
    url = sys.argv[1]
    try:
        res = requests.get(url)
        print(res.text)
    except requests.exceptions.RequestException as er:
        if res.status_code >= 400:
            print(f'Error code: {res.status_code}')
