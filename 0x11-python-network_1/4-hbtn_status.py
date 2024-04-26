#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")


    if r.status_code == 200:
        content = r.text

        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
    else:
        print(f"Error: {response.status_code}")
