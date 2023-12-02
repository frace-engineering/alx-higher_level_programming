#!/usr/bin/python3
""" Python script that takes in a url and an email address, sends
    a post request ti the passed url with email as a parameter, and
    finally displays the body of the reaponse
    """
import requests
import sys


if __name__ == "__main__":
    """Take the url and post the email as data """
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    res = requests.post(url, data=data)
    print(res.text)
