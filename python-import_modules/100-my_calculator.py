#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    import calculator_1 as op
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] == '+':
        res = op.add(int(argv[1]),int(argv[3]))
        print("{} {} {} = {}".format(argv[1],argv[2],argv[3],res))
    elif argv[2] == '-':
        res = op.sub(int(argv[1]),int(argv[3]))
        print("{} {} {} = {}".format(argv[1],argv[2],argv[3],res))
    elif argv[2] == '*':
        res = op.mul(int(argv[1]),int(argv[3]))
        print("{} {} {} = {}".format(argv[1],argv[2],argv[3],res))
    elif argv[2] == '/':
        res = op.div(int(argv[1]),int(argv[3]))
        print("{} {} {} = {}".format(argv[1],argv[2],argv[3],res))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    