# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:04:43 2024.

q: Write a program to generate and print another tuple whose values are even
numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

@author: sushismurf
"""

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = tuple()
for i in a:
    if i % 2 == 0:
        b += (i,)
print(b)
