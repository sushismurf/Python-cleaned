# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:29:48 2024.

q: Write a program which can map() to make a list whose elements are square of
elements in [1,2,3,4,5,6,7,8,9,10].

@author: doga
"""

def squarer(a):
    return a**2
n = [1,2,3,4,5,6,7,8,9,10]
a = map(squarer, n)
print(list(a))
