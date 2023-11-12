#!/usr/bin/python3
"""Defines the square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent the square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the new Square.

        Args:
            size (int): size of the new Square.
            x (int): x coordinate of the new Square.
            y (int): y coordinate of the new Square.
            id (int): identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update Square.

        Args:
            *args (ints): The new attribute values.
                - The 1st argument represents id attribute
                - The 2nd argument represents size attribute
                - The 3rd argument represents x attribute
                - The 4th argument represents y attribute
            **kwargs (dict): The new key/value pairs of attributes.
        """
        if args and len(args) != 0:
            aa = 0
            for arg in args:
                if aa == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif aa == 1:
                    self.size = arg
                elif aa == 2:
                    self.x = arg
                elif aa == 3:
                    self.y = arg
                aa += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
