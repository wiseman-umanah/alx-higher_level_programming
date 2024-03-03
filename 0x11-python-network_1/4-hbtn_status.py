#!/usr/bin/python3
"""
Sends a request and gets body
"""

if __name__ == "__main__":
    import requests

    r = (requests.get("https://alx-intranet.hbtn.io/status")).text
    print("Body response:")
    print(f"\t- type: {type(r)}")
    print(f"\t- content: {r}")
