# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:24:05 2024.

q: The Fibonacci Sequence is computed based on the following formula:


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci
Sequence in comma separated form with a given n input by console.

@author: sushismurf
"""

def fib(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a > 1:
        return fib(a-1) + fib(a-2)
    else:
        pass
n = input("give a non-negative integer: ")
try:
    n = int(n)
    if n >= 0:    
        if n == 0:
            print([0])
        elif n == 1:
            print([1])
        else:
            a = list()
            for i in range(0, n+1):
                a.append(fib(i))
            print(a)
    else:
        raise ValueError
except ValueError:
    print("uh..")
