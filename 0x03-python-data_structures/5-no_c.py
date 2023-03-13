#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string[:]
    x = 0
    for i in my_string:
        if my_string[i] == 'c' or my_string[i] == 'C':
            new_string = new_string[:(i - x)] + my_string[(i + 1)]
            x += 1
        return(new_string)
