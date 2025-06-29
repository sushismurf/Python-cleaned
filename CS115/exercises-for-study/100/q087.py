# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:18:48 2024.

q: Please write a program to print the list after removing delete even
numbers in [5,6,77,45,22,12,24].

@author: sushismurf
"""

o = [5,6,77,45,22,12,24]
p = list()
for i in o:
    if i % 2 == 0:
        p.append(i)
print(p)
