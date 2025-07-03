# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 23:40:06 2023.

@author: doga

Take a list of numbers and make a new list that has only the even elements.
"""

L1 = []

while True:
    userNum = input("please enter an integer (q to stop): ")
    if userNum == 'q':
        break
    try:
        userNum = int(userNum)
    except ValueError:
        print("That's not an integer.")
        break
    L1.append(userNum)

L1copy = list(L1)

for i in L1copy:
    if i % 2 == 1:
        L1.remove(i)

print("the even numbers are: " + f"\n{L1}")
