#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    for i, letter in enumerate(str):
        if i != n:
            result = result + letter
    return result
