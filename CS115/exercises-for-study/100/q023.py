# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:54:30 2024.

q: Write a method which can calculate square value of number

@author: sushismurf
"""

while True:
    a = input("give an integer: ")
    try:
        a = int(a)
        print(a ** 2)
    except ValueError:
        print("that doesn't look like an integer..")
