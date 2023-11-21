#!/usr/bin/python3
"""This module is a class for a Square
"""


class Square:
    """This square class shows how  data is initialized in a class
    Args:
        size (int): This is the size of the defined square that is private
    Raises:
        ValueError: if size is less than or equal to 0
        TypeError: if size is not an integer
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
