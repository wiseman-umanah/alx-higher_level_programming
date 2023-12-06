#!/usr/bin/python3
"""Module that contains function that loads json from file"""
import json


def load_from_json_file(filename):
    """Loads json string from a file

    Args:
        filename: the filename

    Returns:
        returns the json from file
    """
    with open(filename, "r") as fp:
        return json.loads(fp.read())
