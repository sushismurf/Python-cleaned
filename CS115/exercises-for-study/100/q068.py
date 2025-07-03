# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:18:11 2024.

q: Please write a program using generator to print the even numbers between 0
and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

@author: doga
"""

n = input("give a non-negative integer: ")
try:
    n = int(n)
    if n < 0:
        raise ValueError
    elif n % 2 == 1:
        print("not an even number.")
    else:
        a = str()
        for i in range(0, n+1, 2):
            a += str(i) + ', '
        print(a[:-2])
except ValueError:
    print("uh..")
