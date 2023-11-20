#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        length = get_lenList(my_list)
        if x > length:
            x = length
        for i in my_list:
            if counter == x:
                break
            print(i, end="")
            counter += 1
    except TypeError:
        for i in my_list:
            print(i, end="")
            counter += 1
    print("")
    return counter


def get_lenList(my_list=[]):
    counter = 0
    for i in my_list:
        counter += 1
    return counter
