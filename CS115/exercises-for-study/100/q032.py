# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:45:16 2024.

q: Define a function that can accept an integer number as input and print the
"It is an even number" if the number is even, 
otherwise print "It is an odd number".

@author: sushismurf
"""

def oddEven(a):
    if a % 2 == 1:
        return "it's odd"
    elif a % 2 == 0:
        return "it's even"
    else:
        return None
