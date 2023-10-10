#!/usr/bin/python3


"""Define an class Square."""


class Square:
    """Define a private instance size."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square object"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get the size of square"""
        return self.__size

    @property
    def position(self):
        """Get the position of square"""
        return self.__position

    @size.setter
    def size(self, value):
        """Set the size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Set the position of square"""
        error_message = "position must be a tuple of 2 positive integers"
        if (type(value) is not tuple or len(value) != 2):
            raise TypeError(error_message)
        for i in value:
            if not isinstance(value, int) or i < 0:
                raise TypeError(error_message)
        self.__position = value

    def area(self):
        """calculate and return the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """ Print out the square"""
        if self.size == 0:
            print()
        else:
            for count in range(0, self.position[1]):
                print("")
            for i in range(0, self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
