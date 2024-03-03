#!/usr/bin/python3
"""
Sends a request and value
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.put(argv[1], data={"email": argv[2]})
    print(r.text)
