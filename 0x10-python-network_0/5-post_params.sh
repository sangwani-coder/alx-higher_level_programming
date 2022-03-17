#!/bin/bash
# sends a GET request to a URL and displays the body response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
