#!/usr/bin/python3
""" Python script that feetches 
    https://alx-intranet.hbtn.io/status
    """
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    page = requests.get(url)
    print('Body response:')
    print(f'\t- type: {type(page.text)}')
    print(f'\t- content: {page.text}')
