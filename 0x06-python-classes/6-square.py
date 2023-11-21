#!/usr/bin/python3
"""
This module is a class for a Square
"""


class Square:
    """
    This square class shows how  data is initialized in a class
    Args:
        size (int): This is the size of the defined square that is private
        position (tuple): The position of the my_print function in stdout
    Atrributes:
        area: returns the area of the square
        my_print: prints in stdout the square with the character #
    Raises:
        ValueError: if the size is less or equal to 0
        TypeError: if size is not an integer
    """
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
            self.__position = position
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
        for j in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            if self.__size == 0:
                print("")
            else:
                if self.__position[0] != 0:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def position(self):
        """position getter. Gets new value for position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position setter. Assigns new value to position
        """
        e = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple):
            raise TypeError(e)
        elif len(value) != 2:
            raise TypeError(e)
        elif not isinstance(value[0], int) or value[0] < 0:
            raise TypeError(e)
        elif not isinstance(value[1], int) or value[1] < 0:
            raise TypeError(e)
        else:
            self.__position = value
