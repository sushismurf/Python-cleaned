# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:38:22 2024.

q: Please write a program to compress and decompress the string
"hello world!hello world!hello world!hello world!".

@author: sushismurf
"""

import zlib
def comp(x):
    b = x.encode('utf-8')
    c = zlib.compress(b)
    return c
def decomp(x):
    dd = zlib.decompress(x)
    return dd.decode('utf-8')
a = "hello world!hello world!hello world!hello world!"
print(comp(a))
print(decomp(comp(a)))
