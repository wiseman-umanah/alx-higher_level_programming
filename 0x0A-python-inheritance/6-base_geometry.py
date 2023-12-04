#!/usr/bin/python3

"""A class for Geometry"""


class BaseGeometry():
    """Class for goemetry handling

    Attributes:
        area: raises error with a message
    """
    def area(self):
        """Function that raises an Exception
        with the message area() is not implemented

        Raises:
            AttributeError: To tell user that function is not implemented
        """
        raise AttributeError("area() is not implemented")
