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

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_list[satr] = obj[satr]
            return d_list

        return obj
