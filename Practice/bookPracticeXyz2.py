# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 09:27:04 2023.

@author: billypatty
"""

x = input("input an integer: ")
y = input("input another integer: ")
z = input("input another integer: ")
outputValue = min(x, y, z)

if not x.isdigit() or not y.isdigit() or not z.isdigit():
    print("make sure you enter integers.")
else:
    x = int(x)
    y = int(y)
    z = int(z)

if x % 2 == 1:
    outputValue = x
elif y % 2 == 1 and y > outputValue:
    outputValue = y
elif z % 2 == 1 and z > outputValue:
    outputValue = z
else:
    outputValue = max(x, y, z)
    print(f"all numbers are even, and the greatest one is {outputValue}.")

print(f"the greatest odd number is {outputValue}.")
