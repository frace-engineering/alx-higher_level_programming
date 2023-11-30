#!/usr/bin/bash
# Script that takes a url and send a GET  request to it
#+ then displays the size of the body in bytes
curl -sL "$1"
