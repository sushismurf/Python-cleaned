# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:37:12 2024.

q: Write a program which can map() to make a list whose elements are square of
numbers between 1 and 20 (both included).

@author: sushismurf
"""

def squarer(a):
    return a**2
a = map(squarer, range(1,21))
print(list(a))
