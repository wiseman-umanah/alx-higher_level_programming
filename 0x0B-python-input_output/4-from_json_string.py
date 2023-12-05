#!/usr/bin/python3
import json


def from_json_string(my_str):
    """Converts object from JSON to python object"""
    return json.JSONDecoder().decode(my_str)
