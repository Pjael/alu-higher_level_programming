#!/usr/bin/python3
def simple_delete(a_dictionary, key=''):
   j = False
   for p in a_dictionary:
       if p == key:
           j = True
   if j:
        del a_dictionary[key]
   return(a_dictionary)
