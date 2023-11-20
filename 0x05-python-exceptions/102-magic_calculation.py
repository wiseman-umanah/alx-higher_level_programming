#!/usr/bin/python3
def func(a, b):
    result = 0
    for i in range(1, 3, 2):
        try:
            if i > a:
                raise ("Too far")
            else:
                result += a ** b / i
        except IndexError:
            result = a + b
        break
    return result
