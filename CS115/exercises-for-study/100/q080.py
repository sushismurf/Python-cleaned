# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:33:03 2024.

q: Please write a program to randomly generate a list with 5 numbers, which
are divisible by 5 and 7 , between 1 and 1000 inclusive.

@author: sushismurf
"""

import random
a = list()
while len(a) < 5:
    b = random.choice(range(1, 1001))
    if b % 5 == 0 and b % 7 == 0:
        a.append(b)
    else:
        pass
print(a)
