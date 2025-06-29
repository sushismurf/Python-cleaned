# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:17:04 2024.

q: Write a program which can filter even numbers in a list by using filter
function. The list is: [1,2,3,4,5,6,7,8,9,10].

@author: sushismurf
"""

def listFilter():
    a = [1,2,3,4,5,6,7,8,9,10]
    b = list()
    for i in a:
        if i % 2 == 0:
            b.append(i)
    print(b)
listFilter()
