#!/usr/bin/python3
"""Defines a class Rect that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.

        Attributes:
            area: The area of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Function that returns the area of a rectangle

        Returns:
            The area of the rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """Returns the string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
