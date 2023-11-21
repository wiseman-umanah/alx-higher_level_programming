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
        __lt__: Compare 2 squares
        __le__: Compare 2 squares
        __gt__: Compare 2 squares
        __ge__: Compare 2 squares
        __ne__: Compare 2 squares
        __eq__: Compare 2 squares
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
        This resets the size value if the size needs to be changed
        Args:
            value (int): the new value for the size of the Square
        Raises:
            ValueError: if the new value is not an integer
        """
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value >= 0:
            self.__size = value
        else:
            raise ValueError("size must be an integer")

    def __lt__(self, other):
        """Compare 2 squares
        """
        return self.__size < other.__size

    def __gt__(self, other):
        """Compare 2 squares
        """
        return self.__size > other.__size

    def __eq__(self, other):
        """Compare 2 squares
        """
        return self.__size == other.__size

    def __ne__(self, other):
        """Compare 2 squares
        """
        return self.__size != other.__size

    def __ge__(self, other):
        """Compare 2 squares
        """
        return self.__size >= other.__size

    def __le__(self, other):
        """Compare 2 squares
        """
        return self.__size <= other.__size
