#!/usr/bin/python3
"""
This script takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8).

The email is sent in the 'email' variable.

Usage:
    ./2-post_email.py <URL> <email>

Modules:
    urllib.request - For sending HTTP requests.
    urllib.parse - For encoding POST data.
    sys - For handling command-line arguments.

Requirements:
    - Use only urllib and sys.
    - Display the body of the response decoded in utf-8.
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Get URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email into POST data
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    # Send the POST request and display the response
    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode("utf-8")
        print(body)
