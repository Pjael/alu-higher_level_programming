#!/usr/bin/python3
def divisible_by_2(my_list=[]):
        a_list = []
        a_list += my_list
        if my_list:
            for i in range(len(my_list)):
                if (my_list[i] % 2) == 0:
                    a_list[i] = True
                else:
                    a_list[i] = False
        return(a_list)
