#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    key_list = list(a_dictionary.keys())

    for x in key_list:
        if x == key:
            a_dictionary.update({key: value})
        else:
            a_dictionary[key] = value
    return a_dictionary
