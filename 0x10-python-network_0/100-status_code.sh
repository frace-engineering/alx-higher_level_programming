#!/usr/bin/bash
# Bash script that sends a url request and displays only the status code
echo "$(curl -s -w "%{http_code}" $1)" 
