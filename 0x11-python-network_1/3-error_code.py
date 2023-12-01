#!/usr/bin/python3
""" Pyhton script that takes in a url, sends a request
    to the url and displays the body of the rresponse
    """
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    """ Within a try block, take a url and send a request,
        tom the url and display the body of the response
        decoded in utf-8.

        Take care of HTTPError
        """
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            page_content = response.read().decode('utf-8')
        print(f'{page_content}')
    except urllib.error.HTTPError as er:
        print(f'Error code: {er.code}')
