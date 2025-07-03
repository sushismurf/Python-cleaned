# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:48:40 2024.

q: Write a program that computes the value of a+aa+aaa+aaaa with a given
digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

@author: doga
"""

while True:
    a = input("give an integer: ")
    try:
        a = int(a)
        break
    except ValueError:
        print("invalid.")
print(a + a*11 + a*111 + a*1111)
