#!/usr/bin/python3
"""
Write a Python scrip that takes in a URL, sends a request
to the URL and displays the body of the response
"""


from urllib import request
from urllib import error
import sys

if __name__ == '__main__':

    argv = sys.argv
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.status))
