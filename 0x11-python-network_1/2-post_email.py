#!/usr/bin/python3
"""
Sends a request and data to server
"""

if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    values = {"email": argv[2]}
    data = parse.urlencode(values)
    data = data.encode("ascii")
    resp = request.Request(argv[1], data)
    with request.urlopen(resp) as response:
        res = response.read()
    print(res.decode("utf-8"))
