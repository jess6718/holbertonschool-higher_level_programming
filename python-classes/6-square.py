#!/usr/bin/python3


"""Define an class Square."""


class Square:
    """Define a private instance size."""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        error_msg = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(error_msg)
        if len(value) != 2:
            raise TypeError(error_msg)
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError(error_msg)
        if value[0] < 0 or value[1] < 0:
            raise TypeError(error_msg)
        self.__position = value

    def area(self):
        area = self.__size * self.__size
        return area

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for count in range(0, self.position[1]):
                print("")
            for i in range(0, self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
