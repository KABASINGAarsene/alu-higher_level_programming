#!/usr/bin/python3
"""
cnsuivjweo washcwiuasv wdasvweav
wsafwnisafuhSAFJNASF EASFASF
ASFASFNWESAF ASDFIJNSAd fwasg
"""


import urllib.request
import urllib.error
import sys

def fetch_url(url):
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
