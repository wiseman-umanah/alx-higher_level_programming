#!/usr/bin/python3
"""
Defines a class Square that inherits from BaseGeometry.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represent a rectangle using BaseGeometry.
    """
    def __init__(self, size):
        """
        Intialize a new Rectangle.

        Args:
            size (int): The size of the square

        Attributes:
            area: The area of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square
        """
        return pow(self.__size, 2)

    def __str__(self):
        """
        Returns the string reresentation of the class
        """
        return f"[Square] {self.__size}/{self.__size}"
