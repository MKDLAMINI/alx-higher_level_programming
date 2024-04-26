#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request
http://0.0.0.0:5000/search_user
"""


from sys import argv
from requests import post

if __name__ == '__main__':

    URL = 'http://0.0.0.0:5000/search_user'
    information = {'q': argv[1] if len(argv) >= 2 else ""}
    response = post(URL, information)

    diff_response = response.headers['content-type']

    if diff_response == 'application/json':
        output = response.json()
        new_id = output.get('new_id')
        name = output.get('name')
        if (output != {} and new_id and name):
            print("[{}] {}".format(new_id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
