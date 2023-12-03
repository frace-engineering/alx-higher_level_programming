#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = 'http://api.github.com/user'
    r = requests.get(url, auth=(user, passwd))
    r_json = r.json()
    print(f'{r_json.get("id")}')
