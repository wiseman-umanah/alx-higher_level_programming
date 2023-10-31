#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of " + str(number)
if number < 0:
    number = number * -1
    last = number % 10
    if last == 0:
        print(f"Last digit of {number * -1} is {last} and is 0")
    else:
        number = number * -1
        last *= -1
        print(f"{string} is {last} and is less than 6 and 0")
else:
    last = number % 10
    if last == 0:
        print(f"{string} is {last} and is 0")
    elif last > 5:
        print(f"{string} is {last} and is greater than 5")
    elif last < 6:
        print(f"{string} is {last} and is less than 6 and not 0")
