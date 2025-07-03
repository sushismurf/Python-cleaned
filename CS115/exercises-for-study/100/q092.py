# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:42:25 2024.

q: By using list comprehension, please write a program to print the list
after removing the value 24 in [12,24,35,24,88,120,155].

@author: doga
"""

a = [12,24,35,24,88,120,155]
while 24 in a:
    a.remove(24)
print(a)
