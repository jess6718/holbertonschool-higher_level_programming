#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if check_none_val(my_list):
        return None
    return enrich_new_list(my_list)


def check_none_val(my_list):
    if my_list is None or len(my_list) == 0:
        return True
    return False


def enrich_new_list(old_list):
    new_list = []
    for i in range(len(old_list)):
        if old_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
