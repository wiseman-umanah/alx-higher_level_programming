#!/usr/bin/python3
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        res = response.read()
    print(f"Body response:\n\
       \t- type: {type(res)}\n\
       \t- content: {res}\n\
       \t- utf8 content: {res.decode()}"
       )
