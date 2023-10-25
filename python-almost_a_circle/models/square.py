#!/usr/bin/python3
"""Define Sub Class square"""
from models.rectangle import Rectangle


class Square(Rectangle):  # inherite all attribute/var from Rectangle
    """Subclass class init"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initiate instance var"""

        # can also use key:value format "width=size"
        super().__init__(size, size, x, y, id)

    def __str__(self):  # each class has its own __str__
        """print str"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}"

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        # cannot put self.__width due to private, so call etter function
        self.width = value
        self.height = value
