# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:20:42 2023.

@author: billypatty

Write a lambda expression that has two numeric
parameters. If the second argument equals zero, it should return
None. Otherwise it should return the value of dividing the first
argument by the second argument. Hint: use a conditional
expression.
"""

f = lambda x, y: None if y == 0 else x/y

x = int(input("enter x: "))
y = int(input("enter y: "))

print(f(x, y))
