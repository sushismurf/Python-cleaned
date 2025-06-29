# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:55:53 2023.

@author: billypatty

Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.
"""

userNum = input("enter an integer: ")

while userNum != 'no':
    try:
        userNum = int(userNum)
        break
    except ValueError:
        print("thats not an integer.")
        userNum = input("enter an integer: ")

if userNum % 2 == 0:
    print("even")
else:
    print("odd")
