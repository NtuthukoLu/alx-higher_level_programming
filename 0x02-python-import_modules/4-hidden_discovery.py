#!/usr/bin/python3
import sys
import hidden_4
if __name__ == "__main__":
    name = dir(hidden_4)

for _name in name:
    if _name [0:2] != "__":
        print(_name)
