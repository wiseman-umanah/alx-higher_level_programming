#!/usr/bin/python3
"""Module that contains function that loads, add and also save json to file"""
import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"


def main(filename):
    """Loads json, Add json to file, saves

    Args:
        filename: the filename
    """
    listy = []
    i = 1
    while i < len(sys.argv):
        listy.append(sys.argv[i])
        i += 1
    try:
        temp = load(filename)
        listy = list(temp) + listy
        save(listy, filename)
    except FileNotFoundError:
        save(listy, filename)


main(filename)
