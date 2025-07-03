# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:48:22 2024.

q: With a given list [12,24,35,24,88,120,155,88,120,155], write a program to
print this list after removing all duplicate values with original order
reserved.

@author: doga
"""

a = [12,24,35,24,88,120,155,88,120,155]
b = list()
for i in range(len(a)):
    for j in range(len(a)):
        if i == j:
            pass
        else:
            if not a[i] == a[j] and a[i] not in b:
                b.append(a[i])
print(b)
