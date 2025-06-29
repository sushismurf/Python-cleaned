# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:17:40 2024.

q: Write a program that accepts a sentence and calculate the number of
letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

@author: billypatty
"""

def whatThis():
    lCount = 0
    nCount = 0
    a = input("give a sentence, number, whatever you want: ")
    for i in a:
        if i.isalpha():
            lCount += 1
        elif i.isdigit():
            nCount += 1
        else:
            pass
    print('LETTERS', lCount)
    print('NUMBERS', nCount)
whatThis()
