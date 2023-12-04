#!/usr/bin/bash
# Bash script that sends a url request and displays only the status code
curl -s -o /dev/null -w "%{http_code}" "$1" 
