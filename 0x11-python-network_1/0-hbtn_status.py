#!/usr/bin/python3
""" Python script that fetches a url using urllib """
import urllib.request


if __name__ == "__main__":
    """Run the script as the main """
    request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(request) as response:
        html = response.read()
        print('Body response:')
        print('\t - type: {}'.format(type(html)))
        print('\t - content: {}'.format(html))
        print('\t - utf8 content: {}'.format(html.decode('utf-8')))
