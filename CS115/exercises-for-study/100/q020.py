# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:25:06 2024.

q: Define a class with a generator which can iterate the numbers,
which are divisible by 7, between a given range 0 and n.

@author: billypatty
"""

class div(object):
    def __init__(self, n):
        self.n = n
    def iters(self):
        for i in range(0, self.n + 1):
            if i % 7 == 0:
                yield i
while True:
    n = input("give an integer: ")
    try:
        n = int(n)
        break
    except ValueError:
        print("invalid input.")
outs = div(n)
for i in outs.iters():
    print(i)
