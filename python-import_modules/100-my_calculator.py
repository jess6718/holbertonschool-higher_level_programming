#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit (1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if op == "+":
        cal = add(a, b)
    elif op == "-":
        cal = sub(a, b)
    elif op == "*":
        cal = mul(a, b)
    elif op == "/":
        cal = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit (1)
    print("{} {} {} = {}".format(a, op, b, cal))