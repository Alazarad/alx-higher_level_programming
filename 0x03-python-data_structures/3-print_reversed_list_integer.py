#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not isinstance(my_list, list):
        return(my_list)
    a = (len(my_list) - 1)
    for i in range(len(my_list)):
        print("{:d}".format(my_list[a]))
        a -= 1
