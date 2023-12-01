#!/bin/bash
# Displays all HTTP methods the server will accept.
sudo curl -sI "$1" | grep Allow | cut -d " " -f2-
