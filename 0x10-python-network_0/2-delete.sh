#!/bin/bash
# Script that sends a DELETE request to the URL passed as argument and display the reponse
sudo curl -X DELETE "$1"
