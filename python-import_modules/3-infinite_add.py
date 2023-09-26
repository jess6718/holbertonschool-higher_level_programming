#!/usr/bin/python3
import sys

if __name__ == '__main__':
    arg_c = len(sys.argv) - 1
    i = 1 
    total = 0
    while i <= arg_c:
        total = total + int(sys.argv[i])
        i = i + 1
    print("f{total}")
