#!/usr/bin/python3
import sys
if __name__ == '__main__':

    arg_c = len(sys.argv) - 1
    if arg_c > 1:
        print("{} arguments:".format(arg_c))
    elif arg_c == 1:
        print("{} argument:".format(arg_c))
    else:
        print("{} argument.".format(arg_c))
    i = 1
    while i <= arg_c and arg_c > 0:
        print("{}: {}".format(i, sys.argv[i]))
        i = i + 1
