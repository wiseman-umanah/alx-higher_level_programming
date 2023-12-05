#!/usr/bin/python3

"""
A class for Geometry
"""


class BaseGeometry():
    """
    Class for goemetry handling

    Attributes:
        area: raises error with a message
        integer_validator: checks if passed argument is an integer
    """
    def area(self):
        """
        Function that raises an Exception
        with the message area() is not implemented

        Raises:
            AttributeError: To tell user that function is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Functions that validates value

        Args:
            name (str): The type of value parsed
            value (int): the value parsed

        Raises:
            TypeError: value must be an integer
            ValueError: Value must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
