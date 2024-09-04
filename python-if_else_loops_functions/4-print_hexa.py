#!/usr/bin/python3
for i in range(99):
    c = chr((i % 16) + 87) if i % 16 >= 10 else i % 16
    print("{} = 0x{}{}".format(i, int(i / 16), c))
