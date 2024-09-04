#!/usr/bin/python3
for i in range(99):
    if i % 16 >= 10:
        for k in range(97,103):
            if (k % 16) + 9 == i % 16:
                c = chr(k)
    else:
        c = i % 16
    print(f"{i} = 0x{int(i / 16)}{c}")
