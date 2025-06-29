# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 08:53:33 2024.

q: Define a function which can generate and print a tuple where the value are
square of numbers between 1 and 20 (both included). 

@author: sushismurf
"""

def tuple120():
    a = tuple()
    for i in range(1, 21):
        a += (i**2,)
    print(a)
tuple120()
