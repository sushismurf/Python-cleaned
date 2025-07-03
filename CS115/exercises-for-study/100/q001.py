# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:48:59 2024.

q: Write a program which will find all such numbers which are divisible by 7
but are not a multiple of 5, between 2000 and 3200 (both included).
Numbers obtained should be printed in a comma-separated sequence (single line).

@author: doga
"""

numbers = ""

a = 2000

while a <= 3200:
    if a % 7 == 0 and a % 5 != 0:
        numbers += str(a) + ", "
    a += 1

print(numbers[:-2])
