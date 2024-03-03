#!/usr/bin/python3
"""
Sends a request and gets value of a header
"""

if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    req = request.Request(argv[1])
    try:
        request.urlopen(req)
    except error.HTTPError as e:
        print(f"Error code:\t{e.code}")
