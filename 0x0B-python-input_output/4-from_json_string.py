#!/usr/bin/python3
"""Module that contains a funcion that converts JSON to python obj"""
import json


def from_json_string(my_str):
    """Converts object from JSON to python object

    Args:
        my_str (str): the JSON string

    Returns:
        The python object after execution"""
    return json.loads(my_str)
