#!/usr/bin/python3
"""Write a script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id
variable found in the header of the response
"""

import sys, urllib.request


def main():


    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            try:
                x_request_id = response.headers["X-Request-Id"]
                print(x_request_id)
            except KeyError:
                print("X-Request-Id header not found in response.")
    except urllib.error.URLError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
