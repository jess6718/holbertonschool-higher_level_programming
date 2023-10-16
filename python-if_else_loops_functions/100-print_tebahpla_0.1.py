#!/usr/bin/python3
result = ""
for ascii in range(122, 96, -1):
    letter = chr(ascii)
    if ascii % 2 != 0:
        letter = chr(ascii - 32)
    result = result + letter
print("{}".format(result), end="")
