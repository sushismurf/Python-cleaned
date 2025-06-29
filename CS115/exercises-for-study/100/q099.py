# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:23:01 2024.

q: Please write a program which prints all permutations of [1,2,3].

@author: sushismurf
"""

import random
a = [1, 2, 3]
b = []
while len(b) < len(a)*(len(a)-1):
    random.shuffle(a)
    print(a)
    if a not in b:
        b += [a[:]]
b.sort()
print(b)
