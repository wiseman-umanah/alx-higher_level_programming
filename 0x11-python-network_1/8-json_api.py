#!/usr/bin/python3
"""Search using a string
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    letter = "" if len(argv) == 1 else argv[1]
    try:
        r = requests.post("http://0.0.0.0:5000/search_user", json={"q": letter})
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
