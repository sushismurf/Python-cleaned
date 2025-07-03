# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 21:53:05 2024.

q: Define a function which can print a dictionary where the keys are numbers
between 1 and 20 (both included) and the values are square of keys.

@author: doga
"""

# literally the same question as the last one. i'll use a loop this time

def key120():
    a = dict()
    for i in range(1,21):
        a[i] = i**2
    print(a)
key120()
