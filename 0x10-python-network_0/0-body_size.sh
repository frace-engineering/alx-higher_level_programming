#!/bin/bash
# Script that takes a url and sent a request to it
sudo curl -s "$1" | wc -c
