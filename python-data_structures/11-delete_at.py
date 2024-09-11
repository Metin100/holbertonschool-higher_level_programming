#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in range(0, len(my_list)):
        if i == idx:
            my_list.remove(i + 1)
            return my_list
    return my_list
