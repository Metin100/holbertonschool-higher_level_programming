#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    booli = my_list[:]
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            booli[i] = True
        else:
            booli[i] = False
    return booli
