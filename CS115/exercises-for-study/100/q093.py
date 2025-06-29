# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:46:04 2024.

q: With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
write a program to make a list whose elements are intersection of the above
given lists.

@author: sushismurf
"""

a = [1,3,6,78,35,55]
b = [12,24,35,24,88,120,155]
c = list()
for i in a:
    for j in b:
        if i == j:
            c.append(i)
            break
print(c)
