#!/usr/bin/python3
"""
Sends a request and gets value of a header
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get(argv[1])
    print(r.headers.get("X-Request-Id"))
