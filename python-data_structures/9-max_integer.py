#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        this_list = [my_list[0]]
        for i in my_list:
            if i > this_list[0]:
                this_list[0] = i
        return(this_list[0])
    return(None)
