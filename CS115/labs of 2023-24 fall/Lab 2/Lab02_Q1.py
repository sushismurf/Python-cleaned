#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 08:54:48 2023

"""

n = int(input('Enter an integer (-1 to stop): '))

sum_of_fractions = 0.0
for i in range(1, n + 1):
    sum_of_fractions += 1 / i

msg = 'the sum of 1'
for i in range(2, n + 1):
    msg += f' + 1/{i}'

msg += f' is {sum_of_fractions:.3f}'
print(msg)