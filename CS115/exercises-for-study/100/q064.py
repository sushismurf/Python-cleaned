# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:21:17 2024.

q: Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by
console (n>0).

@author: sushismurf
"""

while True:
        n = input("give an integer: ")
        m = 0
        try:
            n = int(n)
            if n>0:
                for i in range(1, n+1):
                    m += 1/i
                print(m)
                break
            else:
                raise ValueError
        except ValueError:
            print("umm..")
