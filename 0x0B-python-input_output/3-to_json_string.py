#!/usr/bin/python3
"""Module that contains function to change object to json"""
import json


def to_json_string(my_obj):
    """Converts object to JSON encoding

    Args:
        my_obj: The object

    Returns:
        returns the json format of the obj
    """
    return json.dumps(my_obj)
