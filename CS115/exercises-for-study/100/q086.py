# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:15:14 2024.

q: Please write a program to generate all sentences where subject is
in ["I", "You"] and verb is in ["Play", "Love"] and the object is in
["Hockey","Football"].

@author: sushismurf
"""

# what the hell

a = ["I", "You"]
b = ["Play", "Love"]
c = ["Hockey", "Football"]
for i in a:
    for j in b:
        for k in c:
            print(i, j, k)
