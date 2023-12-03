#!/usr/bin/python3
"""Python script that takes your github credentials
    username and password and uses the github API to
    display your id
    """
import requests
import sys


if __name__ == "__main__":
    """ run the script as a non_importable module """
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = 'http://api.github.com/user'
    r = requests.get(url, auth=(user, passwd))
    r_json = r.json()
    print(f'{r_json.get("id")}')
