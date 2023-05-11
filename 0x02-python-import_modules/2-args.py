#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    valueArgs = len(argv)
    if valueArgs == 1:
        print("0 arguments.")
    elif valueArgs == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(valueArgs - 1))
    for i in range(1, valueArgs):
        print("{}: {}".format(i, argv[i]))
