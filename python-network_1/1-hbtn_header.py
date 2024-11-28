#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the value
of the 'X-Request-Id' variable found in the header of the response.
"""
import urllib.request
import sys

# Get the URL from the command-line arguments
url = sys.argv[1]

if __name__ == "__main__":

    # fetch the URL using urllib
    with urllib.request.urlopen(url) as response:
        # Get the value of the 'X-Request-ID' header
        request_id = response.headers.get('X-Request-Id')
    
    # print the value of the 'X-Request-Id'
    print(request_id)
