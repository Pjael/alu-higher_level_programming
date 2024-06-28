#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    another_dictionary = {}
    for p, j in a_dictionary.items():
        another_dictionary[p] = j * 2
    return(another_dictionary)
