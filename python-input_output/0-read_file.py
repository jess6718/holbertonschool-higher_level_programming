#!/usr/bin/python3
"""Define a module"""


def read_file(filename=""):
    """Define function that read file"""

    with open(filename, 'r') as file:
        contents = file.read()
        print(contents)
