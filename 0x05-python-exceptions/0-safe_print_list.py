#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cou = 0
    for i in range(x):
        try:
            print("P{}".format(my_list[i]), end="")
            cou += 1
        except IndexError:
            break
    print("")
    return(cou)