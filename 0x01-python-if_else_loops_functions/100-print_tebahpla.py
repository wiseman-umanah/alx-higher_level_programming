#!/usr/bin/python3
for i in range(122, 96, -1):
    print(chr(i - 32) if i in range(121, 96, -2) else chr(i), end="")
