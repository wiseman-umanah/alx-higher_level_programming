#!/usr/bin/python3

"""The Rectangle class for Rectangle instances

imports from Base module
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle Class for creating Rectangle instances

    Attributes:
        area: returns the area of the rectangle

        display: prints the shape of the rectangle to STDOUT

        update: updates the argument of the class

        to_dictionary: creates a dictionary with class instances

        @property:
            width: sets and retrieves the width of the class

            height: sets and retrieves the height of the class

            x: sets and retrieves the x-axis of the class

            y: sets and retrieves the y-axis of the class

    Args:
        id (any): The id from the super class

        width (int): the width of the rectangle

        height (int): the height of the rectangle

        x (int): the x axis to draw the rectangle

        y (int): the y axis to draw the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new instance for class Rectangle

        Args:
            width (int): the width of the rectangle

            height (int): the height of the rectangle

            x (int): the x-axis of the rectangle

            y (int): the y-axis of the rectangle

        Raises:
            TypeError: if height, width, x or y is not an integer

            ValueError: if height, width, x or y is > 0
        """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("x must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the width of the rectangle

        Args:
            value: The new value to set the rectangle's width to

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of the height of the rectangle

        Args:
            value: The new value to set the rectangle's height to

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """returns the x value of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x value of the rectangle

        Args:
            value: The new value to set the rectangle's x-axis to

        Raises:
            TypeError: if x is not an integer
            ValueError: if x is < 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns the y-axis of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y value of the rectangle

        Args:
            value: The new value to set the rectangle's y-axis to

        Raises:
            TypeError: if y is not an integer
            ValueError: if y is < 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle to STDOUT"""
        print((("#" * self.width + "\n") * self.height).strip())

    def __str__(self):
        """Returns the string representation of the class"""
        msg = f"{self.__width}/{self.__height}"
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {msg}"

    def update(self, *args, **kwargs):
        """Updates the instances from dictionary and list"""
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "width" in kwargs:
                self.width = kwargs["width"]

    def to_dictionary(self):
        """Converts the instances to a dictionary

        Returns:
            returns the dictionary of the class
        """
        new_dict = {}
        new_dict["x"] = self.__x
        new_dict["y"] = self.__y
        new_dict["id"] = self.id
        new_dict["height"] = self.__height
        new_dict["width"] = self.__width
        return new_dict
