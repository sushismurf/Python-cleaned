# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:31:00 2024.

q: Please write a program to randomly generate a list with 5 even numbers
between 100 and 200 inclusive.

@author: sushismurf
"""

import random
a = list()
while len(a) < 5:
    b = random.choice(range(100, 201))
    if b % 2 == 0:
        a.append(b)
    else: 
        pass
print(a)
