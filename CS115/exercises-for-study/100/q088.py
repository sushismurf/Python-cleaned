# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:22:49 2024.

q: By using list comprehension, please write a program to print the list after
removing delete numbers which are divisible by 5 and 7 in
[12,24,35,70,88,120,155].

@author: sushismurf
"""

# assuming numbers divisible by only one of them are fine. like 120 can stay
# but 35 has to go

a = [12,24,35,70,88,120,155]
b = list()
for i in a:
    if i % 5 == 0 and i % 7 == 0:
        pass
    else:
        b.append(i)
print(b)
