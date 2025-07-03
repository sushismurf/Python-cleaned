# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:49:19 2024.

q: Please write a program to print the running time of execution of "1+1"
for 100 times.

@author: doga
"""

from timeit import Timer
def b():
    for i in range(0, 100):
        1 + 1
a = Timer(b)
print(a.timeit())
