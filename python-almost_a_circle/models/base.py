#!/usr/bin/python3
"""Base Class"""


class Base:
    """Define Base class init function"""
    __nb_objects = 0  # class var value is updated when instance var access it

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1  # access class var
            self.id = Base.__nb_objects
