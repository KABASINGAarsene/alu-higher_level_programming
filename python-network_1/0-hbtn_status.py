#!/usr/bin/python3
"""
This script fetches the status of the URL "https://alu-intranet.hbtn.io/status"
using urllib and displays the response body in the required format.
"""
import urllib.request

# URL to fetch
url = "https://alu-intranet.hbtn.io/status"

# Fetch the URL using urllib
with urllib.request.urlopen(url) as response:
    body = response.read()

# Display the response details
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))
