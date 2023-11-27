#!/usr/bin/python3
class Rectangle:
    def __init__(self, width= 0, height= 0):
        self.__height = height 
        self.__width = width
    
    @property
    def width(self):
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
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.width) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return (("#" * self.width + "\n") * self.height).strip()
    
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
