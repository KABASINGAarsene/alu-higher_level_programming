#!/usr/bin/python3
"""
This script fetches the status of a given URL using urllib.
"""
import urllib.request

if __name__ == "__main__":
    # Change URL as needed during testing
    url = "http://0.0.0.0:5050/status"

    # Fetch the URL and display the response
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

