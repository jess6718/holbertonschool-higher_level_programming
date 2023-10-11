#!/usr/bin/python3
"""A function that adds 2 integers"""


def add_integer(a, b=98):
    """Adding edge cases"""

    
    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
