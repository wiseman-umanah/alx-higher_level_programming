#!/usr/bin/python3
"""
This module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """
    Class that defines a rectangle
    Attributes:
        area: returns the area of the rectangle
        perimeter: returns the perimeter of the rectangle
        __str__: petty prints the rectangle to satndard output
        __repr__: returns a formal representation of the object
        __del__: prints a statement to stdout whenever a change is made
    """

    number_of_instances = 0
    print_symbol = "#"

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
        rect = ""
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.height):
            rect += (str(self.print_symbol) * self.width) + "\n"
        return rect[:-1]

    def __repr__(self):
        """Returns an official print of the object and its property"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints to stdout if instance is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        The object with the biggest area is returned
        Returns:
            The object that is the biggest or rect_1 if both are the same
            based on their area
        Raises:
            TypeError: if rect1 or rect_2 is not an instance of Rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
         returns a new Rectangle instance with width == height == size
         """
        return Rectangle(size, size)
