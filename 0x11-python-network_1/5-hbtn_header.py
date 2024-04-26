#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request
to the URL and displays the value of the variable X-Request-Id
in the response header
"""


from sys import argv
from requests import get

response = get(argv[1])
print(response.headers.get('X-Request-Id'))
