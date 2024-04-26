#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials (username and password) and uses the GutHun API to display your id
"""


from sys import argv
from requests import get

if __name__ == '__main__':

    username = argv[1]
    password = argv[2]

    URL = "https://api.github.com/user"
    response = get(URL, auth=(username, password))
    json = response.json()

    print(json.get('id'))
