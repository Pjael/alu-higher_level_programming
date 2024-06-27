#!/usr/bin/python3
def no_c(my_string):
    this_string = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            this_string += my_string[i:(i + 1)]
    return(this_string)
