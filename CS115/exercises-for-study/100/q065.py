# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 08:49:53 2024.

q: Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).

@author: doga
"""

# in the original answer, it says that if the input is 5, the output should be
# 500. either of us may be bad at math, but i calculated it to be 501 - and so
# does the code below.. i might have to revisit this one.

def summer(n):
    while True:
        try:
            n = float(n)
            if n == 0:
                return 1
                # break
            elif n < 0:
                print("a positive number please..")
            else:
                return summer(n-1) + 100
                break
        except ValueError:
            print("that doesnt look like a number..")
        n = input("give a number: ")
n = input("give a number: ")
print(summer(n))
