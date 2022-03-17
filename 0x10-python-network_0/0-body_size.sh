#!/bin/bash
# Takes a URL, sends a request and displays the size of the body
curl -sI $1 | grep -i content-length | awk '{print $2}'
