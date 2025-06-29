# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:28:06 2024.

q: Please write a program using generator to print the numbers which can be
divisible by 5 and 7 between 0 and n in comma separated form while n is
input by console.

Example:
If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70

@author: sushismurf
"""

n = input("give an integer: ")
try:
    n = int(n)
    a = str()
    if n >= 0:
        for i in range(0, n):
            if i % 5 == 0 and i % 7 == 0:
                a += str(i) + ', '
            else:
                pass
    else:
        for i in range(n, 0):
            if i % 5 == 0 and i % 7 == 0:
                a += str(i) + ', '
            else:
                pass
    print(a[:-2])
except ValueError:
    print("uh..")
