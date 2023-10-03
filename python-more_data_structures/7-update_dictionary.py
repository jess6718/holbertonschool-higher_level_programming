#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None or len(a_dictionary) == 0:
        a_dictionary[key] = value
        return a_dictionary
    key_list = list(a_dictionary.keys())

    for x in key_list:
        if x == key:
            a_dictionary.update({key: value})
        else:
            a_dictionary[key] = value
    return a_dictionary
