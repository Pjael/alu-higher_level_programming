#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for p, j in a_dictionary.items():
        if p == key:
            a_dictionary[p] = value
            break
    else:
        a_dictionary[key] = value
    return(a_dictionary)
