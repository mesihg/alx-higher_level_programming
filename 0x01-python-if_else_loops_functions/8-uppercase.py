#!/usr/bin/python3

def uppercase(str):
    # prints a string in uppercase
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            i = chr(ord(i) - 32)
        print(f"{i}",end="")
    print("")

