#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""


if __name__ == "__main__":
    from sys import argv
    import requests


    repo = argv[1]
    name = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(name, repo)

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass