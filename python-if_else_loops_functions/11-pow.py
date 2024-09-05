#!/usr/bin/python3
def pow(a, b):
    k = 1
    if b == 0:
        return k
    elif b > 0:
        for i in range(b):
            k *= a
        return k
    elif b < 0:
        for i in range(-b):
            k *= a
        return 1 / k
