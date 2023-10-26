#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """Define Base class init function"""
    __nb_objects = 0  # class var value is updated when instance var access it

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1  # access class var
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return Json str"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return Json dictionary"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Define a function that write object to a text file"""
        file_name = cls.__name__ + ".json"
        dict_list = []
        with open(file_name, "w") as file:  # file is a var for opened file
            if list_objs is None:
                file.write("[]")
            else:
                for item in list_objs:
                    dict_list.append(item.to_dictionary())
                file.write(Base.to_json_string(dict_list))
