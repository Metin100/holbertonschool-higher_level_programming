#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    c = -1
    for i in str:
        c+=1
        if c == n:
            continue
        else:
            new_str += i
    return new_str
