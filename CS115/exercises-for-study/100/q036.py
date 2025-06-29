# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 21:58:31 2024.

q: Define a function which can generate a dictionary where the keys are
numbers between 1 and 20 (both included) and the values are square of keys.
The function should just print the keys only.

@author: sushismurf
"""

def keys120():
    a = dict()
    for i in range(1, 21):
        a[i] = i**2
    print(a.keys())
keys120()
