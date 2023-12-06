#!/usr/bin/python3
""" Module that defines the class Student
"""


class Student:
    """ Class to create student instances

    Methods:
        to_json: returns directory description
    """
    def __init__(self, first_name, last_name, age):
        """ Special method to initialize

        Args:
            first_name: the first name of user
            last_name: the last name of the user
            age: the age of the user
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method that returns directory description """
        return self.__dict__.copy()
