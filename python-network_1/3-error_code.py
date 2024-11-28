#!/usr/bin/python3
"""
This script sends an HTTP GET request to a provided URL, then displays the 
body of the response (decoded in UTF-8). If an HTTP error occurs, it will 
print the HTTP error code.

Usage:
    ./3-error_code.py <URL>

Modules:
    urllib.request - Used to send the HTTP request and fetch the response.
    urllib.error - Used to handle HTTPError exceptions and print error codes.
    sys - Used to retrieve the URL argument from the command-line input.

Exceptions:
    Handles urllib.error.HTTPError and prints the error code associated 
    with the HTTP request failure.

Requirements:
    - The script must handle HTTPError exceptions.
    - Only the `urllib` and `sys` packages are allowed.
    - The script must use the `with` statement to handle the HTTP request.
"""

import urllib.request
import urllib.error
import sys

def fetch_url(url):
    """
    Sends a GET request to the provided URL and prints the body of the response.
    If an HTTPError occurs, it prints the error code.

    Args:
        url (str): The URL to send the GET request to.

    Raises:
        HTTPError: If the server returns an error response, this exception is caught 
                   and the error code is printed.
    """
    try:
        # Open the URL and read the response
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # Handle HTTP errors and print the error code
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    # Read the URL from the command-line arguments
    url = sys.argv[1]
    fetch_url(url)
