#!/usr/bin/python3
def roman_to_int(roman_string):
    num = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    result = 0
    prev_value = 0

    for i in roman_string[::-1]:
        if roman_num[i] >= prev_value:
            result += num[i]
        else:
            result -= num[i]
        prev_value = num[i]

    return result
