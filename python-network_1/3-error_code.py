#!/usr/bin/python3
"""
This is module documentation. feafywefiuwe fwehfw
wewuewhr weghquwheqw rbhqwiuhqwheqw afhiwqheqwe
"""


import requests


if __name__ == "__main__":
    """
    Send a GET request to the specified URL
    """
    response = requests.get("https://alu-intranet.hbtn.io/status")

    # Display the body of the response with tabulation
    print(f"Body response:\n\t{response.text}")
