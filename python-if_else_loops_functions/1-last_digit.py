#!/usr/bin/python3
import random
number = 10
num = number % 10
if number > 0 and num != 0:
    pass
elif number < 0 and num != 0:
    num = -10 + num
else:
    num = 0

print("Last digit of {} is {} ".format(number, num), end="")

if num > 5:
    print("and is greater than 5")
elif num == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
