#!/usr/bin/python3

"""The Square class for Square instances

imports from Rectangle module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class for creating Square instances

    Attributes:
        update: updates the argument of the class
        to_dictionary: creates a dictionary with class instances

        @property:
            size: sets and retrieves the size of the class
            x: sets and retrieves the x-axis of the class
            y: sets and retrieves the y-axis of the class

    Args:
        id (any): The id from the super class
        size (int): the width and height of the square
        x (int): the x axis to draw the rectangle
        y (int): the y axis to draw the rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new instance for class Square

        Args:
            width (int): the width of the square
            height (int): the height of the square
            x (int): the x-axis of the square
            y (int): the y-axis of the square
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Returns the string representation of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of the size of the square

        Args:
            value: The new value to set the square's width to

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be >= 0")
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """Updates the instances from dictionary and list"""
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Converts the instances to a dictionary

        Returns:
            returns the dictionary of the class
        """
        new_dict = {}
        new_dict["id"] = self.id
        new_dict["x"] = self.x
        new_dict["size"] = self.size
        new_dict["y"] = self.y
        return new_dict
