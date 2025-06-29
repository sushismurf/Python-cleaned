# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:05:20 2024.

q: Write a program which can filter() to make a list whose elements are even
number between 1 and 20 (both included).

@author: sushismurf
"""

def isEven(a):
    return a % 2 == 0
a = filter(isEven, range(1,21))
print(list(a))
