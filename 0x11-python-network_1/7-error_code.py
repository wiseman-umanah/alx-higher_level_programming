#!/usr/bin/python3
"""
Sends a request and gets status
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    try:
        r = requests.get(argv[1])
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error code:", r.status_code)
