# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:25:47 2024.

q: By using list comprehension, please write a program to print the list after
removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

@author: sushismurf
"""

a = [12,24,35,70,88,120,155]
b = list()
for i in range(len(a)):
    if i == 0 or i == 2 or i == 4 or i == 6:
        pass
    else:
        b.append(a[i])
print(b)
