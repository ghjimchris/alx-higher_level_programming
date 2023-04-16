#!/usr/bin/python3
"""Base module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ initialize rectangle class

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x
            y (int): y
            id (int): id of rectangle
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter function"""

        return self.__width

    @property
    def height(self):
        """Getter function"""

        return self.__height

    @property
    def x(self):
        """Getter function"""

        return self.__x

    @property
    def y(self):
        """Getter function"""

        return self.__y

    @width.setter
    def width(self, width):
        """Setter function"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Setter function"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """Setter function"""

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """Setter function"""

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of Rectangle"""

        return self.width * self.height

    def display(self):
        """Print rectangle in stdout with character #"""

        for i in range(self.y):
            print()
        for j in range(self.height):
            print(' ' * self.x, end="")
            print('#' * self.width)

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute"""

        arg_list = ["id", "width", "height", "x", "y"]

        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, arg_list[i], args[i])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle"""

        return {"id": self.id, "x": self.x, "y": self.y, "width": self.width,
                                                         "height": self.height}

    def __str__(self):
        """Str representation of rectangle"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
