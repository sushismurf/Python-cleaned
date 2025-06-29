# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 08:41:27 2023.

@author: billypatty

Write a program that examines three variables (x, y, and z) and prints the
largest odd number among them. If none of them are odd, it should print the
smallest value of the three.
"""

x = input("input an integer: ")
y = input("input another integer: ")
z = input("input another integer: ")
numbers = {x, y, z}

if not x.isdigit() or not y.isdigit() or not z.isdigit():
    print("make sure you enter integers.")
else:
    x = int(x)
    y = int(y)
    z = int(z)

if x % 2 == 0 and y % 2 == 0 and z % 2 == 1:
    print(z, "is the only odd number, so you could say it is the largest.")
elif x % 2 == 0 and y % 2 == 1 and z % 2 == 0:
    print(y, "is the only odd number, so you could say it is the largest.")
elif x % 2 == 0 and y % 2 == 1 and z % 2 == 1:
    largest = max(y, z)
    print(f"among {y} and {z}, {largest} is the greater odd number, since {x} \
is even.")
elif x % 2 == 1 and y % 2 == 0 and z % 2 == 0:
    print(x, "is the only odd number, so you could say it is the largest.")
elif x % 2 == 1 and y % 2 == 0 and z % 2 == 1:
    largest = max(x, y)
    print(f"among {x} and {z}, {largest} is the greater odd number, since {y} \
is even.")
elif x % 2 == 1 and y % 2 == 1 and z % 2 == 0:
    largest = max(x, z)
    print(f"among {x} and {y}, {largest} is the greater odd number, since {z} \
is even.")
elif x % 2 == 1 and y % 2 == 1 and z % 2 == 1:
    largest = max(x, y)
    print(f"all numbers are odd, and {largest} is the greatest one.")
else:
    print("neither of these numbers are odd.")
    largest = max(numbers)
    print(largest, "is the largest number among them.")
