#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the value
of the 'X-Request-Id' variable found in the header of the response.

The 'X-Request-Id' header contains a unique identifier for each request,
and this value is provided by the server.

Usage:
    ./1-hbtn_header.py <URL>

Modules:
    urllib.request - For sending HTTP requests.
    sys - For handling command-line arguments.

Requirements:
    - Use only urllib and sys.
    - Display the 'X-Request-Id' header value from the server's response.
"""
import urllib.request
import sys

# Entry point of the script
if __name__ == "__main__":
    # Get the URL from the command-line arguments
    url = sys.argv[1]

    # Fetch the URL using urllib
    with urllib.request.urlopen(url) as response:
        # Get the value of the 'X-Request-Id' header
        request_id = response.headers.get('X-Request-Id')

    # Print the value of the 'X-Request-Id'
    print(request_id)

