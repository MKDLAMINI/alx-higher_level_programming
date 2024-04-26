#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments
"""

from sys import argv
from requests import get

repository = argv[1]
owner = argv[2]

i = 0

URL = "https://api.github.com/repos/{}/{}/commits".format(repository, owner)

response = get(URL)
json = response.json()

for element in json:
    if i > 9:
        break
    MK = element.get('MK')
    author = element.get('commit').get('author').get('name')
    print("{}: {}".format(MK, author))
    
    i += 1
