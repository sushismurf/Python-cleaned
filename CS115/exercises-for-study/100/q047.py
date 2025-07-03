# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:56:31 2024.

q: Write a program which can map() and filter() to make a list whose elements
are square of even number in [1,2,3,4,5,6,7,8,9,10].

@author: doga
"""

def squarer(a):
    return a**2
def isEven(a):
    return a % 2==0
n = [1,2,3,4,5,6,7,8,9,10]
m = map(squarer, filter(isEven, n))
print(list(m))
