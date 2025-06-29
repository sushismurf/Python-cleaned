# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:40:35 2024.

q: Write a program which accepts a sequence of comma-separated numbers from
console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

@author: billypatty
"""

a = input("give a number (-1 to stop): ")
someList = []
while a != '-1':
    try:
        a = int(a)
        someList.append(a)
    except ValueError:
        print("that ain't no number")
    a = input("give a number (-1 to stop): ")
print(someList)
print(tuple(someList))
