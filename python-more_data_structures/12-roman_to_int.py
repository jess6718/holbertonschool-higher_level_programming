#!/usr/bin/python3
def roman_to_int(roman_string):
    roamn_dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
        }
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    
    total = 0
    pre_val = 0

    # if letter in str cannot be found in dictionary
    for i in reversed(roman_string):
        current_val = roamn_dict[i]

        if current_val >= pre_val:
            total += current_val
        else:
            total -= current_val
        pre_val = current_val
    return total
