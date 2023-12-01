#!/bin/bash
# Script that takes a url and sent a request to it
#+ then displays the size of the body in bytes
curl -s "$1" | wc -c
