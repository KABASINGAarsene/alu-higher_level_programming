#!/usr/bin/python3
"""
This is a module documentation. sdbhsaudsad
asfasfnasfbashfasfsa sajfsafsfs sfdsfdfdsg
"""


import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API URL to get user information
    url = "https://api.github.com/user"

    # Send a GET request with Basic Authentication
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        # Parse the JSON response and print the user ID
        print(response.json().get("id"))
    else:
        # If authentication fails or user is not found, print None
        print("None")
