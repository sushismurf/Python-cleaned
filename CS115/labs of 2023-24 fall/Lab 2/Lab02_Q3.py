#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 10:20:02 2023

"""

s = input('Enter a string (exit to stop): ')

while s.upper() != 'EXIT':
    result = ''
    for i in range(len(s)):
        ch = s[i]
        if i == 0 or ch != s[i - 1]:
            result += ch

    print('adjacent duplicates removed: ', result)
    s = input('Enter a string (exit to stop): ')

print('Bye.')