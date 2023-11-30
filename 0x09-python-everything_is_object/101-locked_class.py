#!/usr/bin/python3
"""
    101-locked_class: class LockedClass
"""


class LockedClass:
    """
        Prevents the user from dynamically creating new instance attributes
        Except if the new instance attribute is called first_name
        Attribute:
             first_name (str): name
    """
    __slots__ = ['first_name']
