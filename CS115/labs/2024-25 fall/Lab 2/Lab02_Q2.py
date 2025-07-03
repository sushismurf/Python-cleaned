#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:01:39 2024

"""

s = input('Enter a string: ')
new_s = ''
for ch in s:
    if not ch.isalpha():
        new_s += '*'
    else:
        new_s += ch
print('New string:', new_s)

# using a for loop that iterates through a range
new_s = ''
for i in range(len(s)):
    ch = s[i]
    if not ch.isalpha():
        new_s += '*'
    else:
        new_s += ch
print('New string:', new_s)