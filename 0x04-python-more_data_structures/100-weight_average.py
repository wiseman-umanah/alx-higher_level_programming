#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    avg1, avg2 = 0, 0
    for i in my_list:
        a, b = i
        avg1 += a * b
        avg2 += b
    avg3 = avg1/avg2
    return avg3
