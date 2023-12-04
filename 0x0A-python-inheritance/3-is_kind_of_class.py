#!/usr/bin/python3

"""returns True if the object is an instance of
or if the object is an instance of a class that inherited from,"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance
    or if object is a class that inherited from the specified class
    otherwise False

    Args:
        obj (object): The object to validate
        a_class (class): The class to use for validity
    Returns:
        True if object is an instance
        False if object is not an intaznce of specified class"""
    if isinstance(obj, a_class):
        return True
    return False
