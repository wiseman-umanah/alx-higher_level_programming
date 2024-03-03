#!/usr/bin/python3
"""
Sends a request and gets value of a header
"""

if __name__ == "__main__":
    from urllib import request
    from sys import argv

    with request.urlopen(argv[1]) as response:
        res = response.headers
    print(res["X-Request-Id"])
