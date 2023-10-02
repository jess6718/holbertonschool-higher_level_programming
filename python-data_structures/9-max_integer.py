#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    for i in range(len(my_list) - 2):
        if my_list[i] > my_list[i + 1]:
            a = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = a
    return my_list[i + 1]
