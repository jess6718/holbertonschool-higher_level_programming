#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_empty(my_list)
    return enrich_new_list(my_list)


def check_empty(test_list):
    if test_list is None or len(test_list) == 0:
        return None


def enrich_new_list(old_list):
    new_list = []
    for i in range(len(old_list)):
        if old_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
