#!/usr/bin/python3
"""Define Sub Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Subclass class init"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiate instance var"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)  # access Base class def

    @property
    def width(self):
        """get width"""
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @property
    def x(self):
        """get x"""
        return self.__x

    @property
    def y(self):
        """get y"""
        return self.__y
