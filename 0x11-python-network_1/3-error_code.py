#!/usr/bin/python3
""" Sends a request to the URL and displays the body of the response
    decoded in uft-8)
"""
from sys import argv
import urllib.request as req
import urllib.parse as parse
import urllib.error as error

if __name__ == "__main__":
    url = argv[1]

    request = req.Request(url)
    try:
        with req.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
