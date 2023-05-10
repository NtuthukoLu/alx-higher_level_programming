#!/usr/bin/python3
def uppercase(str):
    _Str = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            _Str = _Str + chr(ord(char) - 32)
        else:
            _Str = _Str + char
    print("{}".format(_Str))
