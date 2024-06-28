#!/usr/bin/python3
def uppercase(str): 
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            newA = ord(str[i]) + (ord('A') - ord('a'))
        else:
            newA = ord(str[i])
        print("{}".format(chr(newA)), end='')
    print()
