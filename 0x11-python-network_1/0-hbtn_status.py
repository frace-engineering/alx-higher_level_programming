#!/usr/bin/python3
""" Python script that fetches a url using urllib """
import urllib.request


if __name__ == "__main__":
    """Use urllib to fetch the url """
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
    print('Body response:')
    print(f'\t- type: {type(html)}')
    print(f'\t- content: {html}')
    print(f'\t- utf8 content: {html.decode()}')
