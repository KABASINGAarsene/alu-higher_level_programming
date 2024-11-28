#!/usr/bin/python3
"""
This script sends an HTTP GET request to a provided URL, then displays the 
body of the response (decoded in UTF-8). If an HTTP error occurs, it will 
print the HTTP error code.

Usage:
    ./3-error_code.py <URL>

Modules:
    urllib.request - For sending HTTP requests.
    urllib.error - For managing HTTP errors.
    sys - For handling command-line arguments.

Exceptions:
    Handles urllib.error.HTTPError and prints the error code.

Requirements:
    - Must handle HTTPError exceptions.
    - Use only urllib and sys.
    - Must use the 'with' statement for making the request.
"""
import urllib.request
import urllib.error
import sys

def fetch_url(url):
    """
    This function takes a URL, sends a GET request, and displays the response body.
    If an HTTPError occurs, it will print the error code.

    Args:
        url (str): The URL to send the GET request to.
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
