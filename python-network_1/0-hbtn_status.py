#!/usr/bin/python3
"""  fetches https://alu-intranet.hbtn.io/status  """
import urllib.request

url = 'https://intranet.hbtn.io/status'
if url.startswith('https://'):
    url = "https://alu-intranet.hbtn.io/status"

if __name__ == "__main__":
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as resp:
        content = resp.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode("utf-8"))
