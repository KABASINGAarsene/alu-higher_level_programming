#!/usr/bin/python3
"""
This script fetches the URL https://alu-intranet.hbtn.io/status
using urllib and displays the body of the response.
"""
import urllib.request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"

    # Using `with` statement to ensure proper resource management
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

