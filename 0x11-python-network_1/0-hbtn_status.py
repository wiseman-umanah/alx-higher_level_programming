#!/usr/bin/python3
"""Prints out Useful details of the web page
and status"""


if __name__ == "__main__":
    from urllib import request

    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        res = response.read()
    print("Body response:")
    print(f"\t- type: {type(res)}")
    print(f"\t- content: {res}")
    print(f"\t- utf8 content: {res.decode('utf-8')}")
