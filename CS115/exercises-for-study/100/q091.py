# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:37:38 2024.

q: By using list comprehension, please write a program to print the list after
removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

@author: doga
"""

a = [12,24,35,70,88,120,155]
b = list()
for i in range(len(a)):
    if i == 0 or i == 4 or i == 5:
        pass
    else:
        b.append(a[i])
print(b)
