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
    email = sys.argv[2].encode('utf-8')
    param = urllib.parse.urlencode({'email': email})
    full_url = f'{url}?{param}'
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as response:
        page_content = response.read().decode('utf-8')
    print(f'Your email is: {page_content}')
