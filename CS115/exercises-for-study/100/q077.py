# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:13:14 2024.

q: Please write a program to output a random number, which is divisible by 5
and 7, between 0 and 10 inclusive using random module and list comprehension.

@author: sushismurf
"""

# this question makes no sense to me. the only thing it can output is 0 since
# that is the only number divisible by both 5 and 7 between 0 and 10.

import random
a = random.choice(range(0, 11))
while a % 5 != 0 or a % 7 != 0:
    a = random.choice(range(0, 11))
print(a)
