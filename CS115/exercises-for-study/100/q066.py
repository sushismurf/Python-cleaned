# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:15:55 2024.

q: The Fibonacci Sequence is computed based on the following formula:


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input
by console.

@author: doga
"""

def f(n):
    while True:
        try:
            n = int(n)
            if n == 0:
                return 0
            elif n == 1:
                return 1
            elif n >1:
                return f(n-1) + f(n-2)
            else:
                raise ValueError
        except ValueError:
            print("a non-negative integer please..")
n = input("give an integer: ")
print(f(n))
