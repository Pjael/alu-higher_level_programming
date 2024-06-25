#!/usr/bin/python3
def uppercase(str): 
    for i in str:
        p = i
        if ord(p) >= 97 and ord(p) <= 122:
            p = chr(ord(i) - 32)
    print("{}".format(p), end='')
    print()
