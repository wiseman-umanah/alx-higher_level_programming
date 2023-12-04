#!/usr/bin/python3

"""returns True if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """function that returns True
    if the object is exactly an instance of the specified class;
    otherwise False

    Args:
        obj (object): The object to check for validity
        a_class (class): The specified object name
    Returns:
        True if obj is an instance of class
        False if obj is not an instance of class
    """
    if obj.__class__ == a_class:
        return True
    return False
