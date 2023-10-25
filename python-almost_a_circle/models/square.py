#!/usr/bin/python3
from models.rectangle import Rectangle
"""Define Sub Class square"""


class Square(Rectangle):  # inherite all attribute/var from Rectangle
    def __init__(self, size, x=0, y=0, id=None):
        # can also use key:value format "width=size"
        super().__init__(size, size, x, y, id)

    def __str__(self):  # each class has its own __str__
        return f"[Square] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}"
