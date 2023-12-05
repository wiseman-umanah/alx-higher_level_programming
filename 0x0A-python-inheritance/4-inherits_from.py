#!/usr/bin/python3

"""
returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    A Function that
    returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    otherwise False.

    Args:
        obj (object): The object for validation
        a_class (class): the class to use for validation

    Returns:
        True if obj is an instance or subinstance
        False if obj is not an instance or subinstance
    """
    if obj.__init_subclass__ == a_class:
        return True
    return False
