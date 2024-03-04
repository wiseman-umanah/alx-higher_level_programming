#!/usr/bin/python3
"""Github Api with Python via CLI
Authenticates with username, password
Usage: ./10-my_github <username> <password>
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    name = argv[1]
    passwd = argv[2]
    auth = HTTPBasicAuth(name, passwd)
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
