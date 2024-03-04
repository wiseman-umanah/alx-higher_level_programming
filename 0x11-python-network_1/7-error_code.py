#!/usr/bin/python3
"""
Sends a request and gets status
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)
