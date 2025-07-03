#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 09:25:20 2023

"""

n1 = int(input('Enter the first integer: '))
n2 = int(input('Enter the second integer: '))

print('[', end='')
if n1 == n2:
    print(n2, ']')
elif n1 < n2:
    for i in range(n1, n2):
        print(i, end=', ')
    print(n2, ']', sep='')
else:
    for i in range(n1, n2, -1):
        print(i, end=', ')
    print(n2, ']', sep='')  
