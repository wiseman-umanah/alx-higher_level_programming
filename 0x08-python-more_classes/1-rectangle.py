#!/usr/bin/python3
"""
1-rectangle: class Rectangle
"""


class Rectangle:
    """
    This defines a rectangle class with width and height
    """
    def __init__(self, width=0, height=0):
        """
        Initialiizes class with it's instances
        Args:
            height (int): This is the height of the rectangle
            width (int): This is the width of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """sets the width of the rectangle
        Raises:
            ValueError: if width is < 0
            TypeError: if width is not an integer
        Returns:
            Returns the new width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Sets the height of the rectangle
        Raises:
            ValueError: if height is < 0
            TypeError: if height is not an integer
        Returns:
            Returns the new width
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
