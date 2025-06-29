# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:47:00 2023.

@author: billypatty

Create a program that asks the user for a number and then prints out a list of
all the divisors of that number.
"""

userNum = input("enter an integer: ")
myList = []

try:
    userNum = int(userNum)
    for i in range(1, userNum + 1):
        if userNum % i == 0:
            myList.append(i)
    print(myList)
except ValueError:
    print("thats not an integer.")
