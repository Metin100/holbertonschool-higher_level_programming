#!/usr/bin/python3
i = 122
while i > 96:
    print("{}{}".format(chr(i), chr(i - 33)), end="")
    i -= 2
