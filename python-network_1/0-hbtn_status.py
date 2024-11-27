#!/usr/bin/python3
"""
This script fetches the status of a given URL using urllib and displays the response body.
It includes proper error handling to manage cases where the URL is unreachable or encounters an HTTP error.
"""
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))
    except urllib.error.URLError as e:
        print(f"Error: Unable to fetch URL {url}")
        print(f"Reason: {e.reason}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
