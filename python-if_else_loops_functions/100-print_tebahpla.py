#!/usr/bin/python3
for ascii in range(122, 96, -1):
    letter = chr(ascii)
    if ascii % 2 != 0:
        letter = chr(ascii - 32)
    print("{}".format(letter), end="")
