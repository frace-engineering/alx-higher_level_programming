#!/usr/bin/python3
# Python script that fetches a url using urllib
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    http = response.read()
