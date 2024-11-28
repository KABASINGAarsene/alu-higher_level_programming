#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the value
of the 'X-Request-Id' variable found in the header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    # Get the URL from the command line argument
    url = sys.argv[1]

    # Fetch the URL using urllib
    with urllib.request.urlopen(url) as response:
        # Get the value of the 'X-Request-Id' header
        request_id = response.getheader('X-Request-Id')

    # Print the value of 'X-Request-Id'
    print(request_id)
