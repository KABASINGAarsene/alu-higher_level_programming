#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the body
of the response (decoded in utf-8). If an HTTPError exception occurs, it prints
the error code.

Usage:
    ./3-error_code.py <URL>

Modules:
    urllib.request - For sending HTTP requests.
    urllib.error - For managing HTTP errors.
    sys - For handling command-line arguments.

Requirements:
    - Handle urllib.error.HTTPError exceptions.
    - Display the HTTP error code when an exception is raised.
    - Use only urllib and sys.
    - Must use the with statement.
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    # Get URL from the command-line argument
    url = sys.argv[1]

    try:
        # Send the GET request
        with urllib.request.urlopen(url) as response:
            # Read the response and decode it
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        # Handle HTTP errors by printing the error code
        print(f"Error code: {e.code}")
