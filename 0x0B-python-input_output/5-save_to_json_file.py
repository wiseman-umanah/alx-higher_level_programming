#!/usr/bin/python3
"""This module is to transform objects to JSON fomat
and save them to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file
    using a JSON representation

    Args:
        my_obj (object): a python object to change to json
        filename (file): The filename to save to
    """
    with open(filename, "w") as fp:
        fp.write(json.dumps(my_obj))
