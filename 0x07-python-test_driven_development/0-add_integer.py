#!/usr/bin/python3

"""
define an integer addition function
>>>add_integer(5, 6)
11
"""


def add_integer(a, b=98):
    """
    Returns the addition of a and b in function
    Parameters: a and  b, b is 98 if not given
    Raise TypeError if a or b is not an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
