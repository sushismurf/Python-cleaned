# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 22:21:08 2024.

q: Define a function which can generate a list where the values are square of
numbers between 1 and 20 (both included). Then the function needs to print the
last 5 elements in the list.

@author: sushismurf
"""

def list120():
    a = list()
    for i in range(1, 21):
        a.append(i**2)
    print(a[15:])
list120()
