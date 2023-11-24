#!/usr/bin/python3

"""
define a function that prints a square pattern
>>>print_square(3)
###
###
"""


def print_square(size):
    """
    Prints the square pattern based on input
    Parameters: size - size of the square
    Errors: TypeError and ValueError checks
    """
    if not isinstance(size, float) and not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        size = int(size)
        if size >= 0:
            for i in range(size):
                for t in range(size):
                    print("#", end="")
                print("")
        elif size < 0:
            raise ValueError("size must be >= 0")
