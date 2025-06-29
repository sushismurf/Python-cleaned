# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:25:42 2024.

q: Please write a program to generate a list with 5 random numbers between
100 and 200 inclusive.

@author: sushismurf
"""

import random
a = list()
while len(a) < 5:
    b = random.choice(range(100,201))
    a.append(b)
print(a)
