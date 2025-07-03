# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:18:49 2024.

q: Please write a program which accepts a string from console and print the
characters that have even indexes.

ex:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

@author: doga
"""

a = input("say somethin': ")
b = str()
for i in range(len(a)):
    if i % 2 == 0:
        b += a[i]
print(b)
