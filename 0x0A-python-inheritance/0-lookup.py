#!/usr/bin/python3

"""returns the list of available attributes and methods of an object"""


def lookup(obj):
    """Function that returns the list of available
    attributes and methods of an object

    Attributes:
        obj (object): the class object
    Returns:
        list of class attributes
    """

    return dir(obj)
