# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:21:51 2023.

@author: billypatty

Write a program that asks the user to enter an
integer and prints two integers, root and pwr, such that 1 < pwr < 6
and root**pwr is equal to the integer entered by the user. If no such
pair of integers exists, it should print a message to that effect.
"""

userNumber = input("please enter an integer: ")
idkWtf = None

if userNumber.isnumeric():
    userNumber = int(userNumber)
else:
    print("that's not an integer.")

found = False

for root in range(1, userNumber):
    for power in range(2, 6):
        if root ** power == userNumber:
            found = True
            print(f"{root} to the power of {power} is {userNumber}.")
            break

if not found:
    print("no such integer combination exists.")
