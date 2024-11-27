#!/usr/bin/python3
"""
This script fetches the status of a URL using urllib and displays the response body.
The script prints:
    - The type of the response body.
    - The content of the body in bytes.
    - The content decoded as a UTF-8 string.
The URL can be changed to test different endpoints.
"""
import urllib.request

# URL to fetch
url = "http://0.0.0.0:5050/status"

# Fetch the URL using urllib
with urllib.request.urlopen(url) as response:
    body = response.read()

# Display the response details
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))
