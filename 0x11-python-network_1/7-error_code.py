#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response
"""


from requests import get
from sys import argv


if __name__ == "__main__":

    if len(argv) != 2:

        print("Usage: ./script.py <URL>")
        exit(1)

    url = argv[1]
    response = get(url)

    if response.status_code >= 400:

        print(f"Error: {response.status_code}")
    else:
        print(response.text)
