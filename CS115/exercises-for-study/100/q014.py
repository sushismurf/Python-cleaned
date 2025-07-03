# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:25:34 2024.

q: Write a program that accepts a sentence and calculate the number of
upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

@author: doga
"""

def upLow():
    lCount = 0
    uCount = 0
    a = input("give a sentence: ")
    for i in a:
        if i.islower():
            lCount += 1
        elif i.isupper():
            uCount += 1
        else:
            pass
    print('UPPER CASE', uCount)
    print('LOWER CASE', lCount)
upLow()
