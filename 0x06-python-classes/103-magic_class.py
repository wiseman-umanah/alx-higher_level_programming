#!/usr/bin/python3
import math


class MagicClass:

    """Class that stores the properties
    of a circumference"""
    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    """Calculates the area of the circle"""
    def area(self):
        return (self.__radius ** 2) * math.pi

    """Calculates the circumference of the circle"""
    def circumference(self):
        return (2 * math.pi) * self.__radius
