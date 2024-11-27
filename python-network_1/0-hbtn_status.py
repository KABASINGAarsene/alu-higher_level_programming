#!/usr/bin/python3
"""
This script fetches the status of a given URL using urllib and displays the response body.
It defaults to "https://alu-intranet.hbtn.io/status" if no URL is specified.
The script prints:
    - The type of the response body.
    - The content of the body in bytes.
    - The content decoded as a UTF-8 string.
The script ensures compliance with PEP 8 standards and uses only the urllib module.
"""
import urllib.request
import sys

# Default URL
url = "https://alu-intranet.hbtn.io/status"

# Use URL from argument if provided
if len(sys.argv) > 1:
    url = sys.argv[1]

# Fetch the URL using urllib
with urllib.request.urlopen(url) as response:
    body = response.read()

# Display the response details
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))
