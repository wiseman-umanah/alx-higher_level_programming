#!/usr/bin/python3
"""
This module is a class for a Square
"""


class Square:
    """
    This square class shows how  data is initialized in a class
    Args:
        size (int): This is the size of the defined square that is private
    Atrributes:
        area: returns the area of the square
        my_print: prints in stdout the square with the character #
    Raises:
        ValueError: if the size is less or equal to 0
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

    def area(self):
        """this function returns the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        size getter. Handle size errors
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter. Sets the value of size
        """
        if isinstance(value, int) and value >= 0:
            self.__size = value
        else:
            raise ValueError("size must be an integer")

    def my_print(self):
        """prints in stdout the square with the character #
        """
        for i in range(self.__size):
            print("#" * self.__size)
