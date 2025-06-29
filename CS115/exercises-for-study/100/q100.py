# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:42:39 2024.

q: Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?

@author: sushismurf
"""

def cr(h, f):
    for i in range(0, h+1):
        j = h - i
        if 2*i+4*j == f:
            return i, j
a = cr(35, 94)
print(a)
