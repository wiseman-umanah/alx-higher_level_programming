#!/usr/bin/python3
"""
This module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """ Class that defines a rectangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance\n
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ method that returns the value of the width
        Returns:
            width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines the width
        Args:
            value: width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that returns the value of the height
        Returns:
            height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the height
        Args:
            value: height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.width) * 2

    def __str__(self):
        """Returns a pretty print of the rectangle with '#'"""

        if self.width == 0 or self.height == 0:
            return ""
        return (("#" * self.width + "\n") * self.height).strip()

    def __repr__(self):
        """Returns an official print of the object and its property"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints to stdout if instance is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
