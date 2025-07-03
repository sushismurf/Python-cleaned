# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:54:06 2024.

q: Define a function that can accept two strings as input and print the string
with maximum length in console. If two strings have the same length, then the
function should print all strings line by line.

@author: doga
"""

def strLen(a, b):
    if len(a) == len(b):
        print(f'a\nb')
    elif len(a) < len(b):
        print(b)
    elif len(a) > len(b):
        print(a)
    else:
        print("????")
