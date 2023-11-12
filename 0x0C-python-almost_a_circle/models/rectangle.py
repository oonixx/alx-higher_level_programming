#!/usr/bin/python3
"""Defines the rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent the rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the new Rectangle.

        Args:
            width (int): width of the new Rectangle.
            height (int): height of the new Rectangle.
            x (int): x coordinate of the new Rectangle.
            y (int): y coordinate of the new Rectangle.
            id (int): identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height of width is not an int.
            ValueError: If either of width or height of width <= 0.
            TypeError: If either of x or y not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get a width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get a height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get a x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get a y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return an area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update Rectangle.

        Args:
            *args (ints): The new attribute values.
                -The 1st argument represents id attribute
                -The 2nd argument represents width attribute
                -The 3rd argument represent height attribute
                -The 4th argument represents x attribute
                -The 5th argument represents y attribute
            **kwargs (dict): The new key/value pairs of attributes.
        """
        if args and len(args) != 0:
            aa = 0
            for arg in args:
                if aa == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif aa == 1:
                    self.width = arg
                elif aa == 2:
                    self.height = arg
                elif aa == 3:
                    self.x = arg
                elif aa == 4:
                    self.y = arg
                aa += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
