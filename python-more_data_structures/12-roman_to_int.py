#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

    total = 0
    pre_val = 0

    for i in reversed(roman_string):
        current_val = roman_dict[i]

        if current_val >= pre_val:
            total += current_val
        else:
            total -= current_val
        pre_val = current_val
    return total
