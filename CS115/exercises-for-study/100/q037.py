# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 22:04:11 2024.

q: Define a function which can generate and print a list where the values are
square of numbers between 1 and 20 (both included).

@author: doga
"""

def list120():
    a = list()
    for i in range(1,21):
        a.append(i**2)
    print(a)
list120()
