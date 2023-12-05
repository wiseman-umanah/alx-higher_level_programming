#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """Converts object to JSON encoding"""
    return json.JSONEncoder().encode(my_obj)
