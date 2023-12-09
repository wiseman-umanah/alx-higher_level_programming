#!/usr/bin/python3

"""The Base class for Square and Rectangle instances

imports from json, csv and turtle modules
json: to handle all json functionalities in class
csv: to handle all csv functionalities in class
turtle: to handle drawing in python canvas
"""
import json
import csv
from turtle import *


class Base:
    """Base Class for creating Square and Rectangle instances

    Attributes:
        @classmethods:
            increase_nb: This increases when a new instance is created
            save_to_file: This saves an instance creation to a JSON file
            create: creates a dictionary from the instances
            load_from_file: This loads an instance from a JSON file
            save_to_file_csv: This save instances to a CSV file
            load_from_file_csv: This loads an instance from a CSV file

        @staticmethods:
            to_json_string: converts a dictionary to a JSON format
            from_json_string: converts json string to python object
            draw: Draws shape from instance

    Args:
        id (any): The id of each instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an id for an instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def count(self):
        return Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a dictionary to a json format"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves an instance to a JSON file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jFile:
            if list_objs is None:
                jFile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jFile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Converts a json string to a python object"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a dictionary representation of the instance"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                newIns = cls(1, 1)
            else:
                newIns = cls(1)
            newIns.update(**dictionary)
            return newIns

    @classmethod
    def load_from_file(cls):
        """Loads the instance from a JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves an instance to CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads instance from a CSV file """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws the shape of the instance

        Args:
            list_rectangles: rectangle list to draw from
            list_squares: square list to draw from
        """
        if list_rectangles is not None:
            for ins in list_rectangles:
                penup()
                pensize(2)
                hideturtle()
                goto(ins.x, ins.y)
                bgcolor("orange")
                color("red", "lightblue")
                begin_fill()
                pendown()
                for i in range(2):
                    forward(ins.width)
                    right(90)
                    forward(ins.height)
                    right(90)
                end_fill()
                exitonclick()

        if list_squares is not None:
            for ins in list_squares:
                penup()
                pensize(3)
                hideturtle()
                goto(ins.x, ins.y)
                bgcolor("orange")
                color("red", "lightblue")
                begin_fill()
                pendown()
                for i in range(2):
                    forward(ins.width)
                    right(90)
                    forward(ins.height)
                    right(90)
                end_fill()
                exitonclick()
