# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:00:14 2023.

@author: billypatty
"""

x = int(input("please input a positive integer: "))
low, high = 0, max(1, x)
guess = (high + low) / 2

while abs(guess ** 2 - x) >= 0.00001:
    if guess ** 2 > x:
        high = guess
    elif guess ** 2 < x:
        low = guess
    else:
        print("the value is close to", guess)
    guess = (high + low) / 2

print("the value", guess, "squared is close to", f'{x}.')
