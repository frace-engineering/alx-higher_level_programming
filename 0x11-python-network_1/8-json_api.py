#!/usr/bin/python3
""" Python script that takes in a letter and sends
    a post request to http://0.0.0.0:5000/search_user
    with the letter as a parameter
    """
import requests
import sys


if __name__ == "__main__":
    """ Take a url and post data to it,
        retrieve the json representation of the id and name
        """
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    post_data = {'q': letter}
    res = requests.post(url, data=post_data)
    try:
        response = res.json()
        if res.json() == {}:
            print('No result')
        else:
            print(f'[{response.get("id")}] {response.get("name")}')
    except ValueError:
        print('Not a valid JSON')
