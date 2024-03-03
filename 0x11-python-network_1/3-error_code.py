#!/usr/bin/python3
"""
Sends a request and gets error status
"""

if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    try:
        with request.urlopen(argv[1]) as response:
            res = response.read()
        print(res.decode("utf-8"))
    except error.HTTPError as e:
        print("Error code:", e.code)
