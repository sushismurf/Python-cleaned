# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 14:31:03 2024.

q: Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

@author: doga
"""

def isNum(a):
    try:
        a = int(a)
        if a >= 0:
            return True
        else:
            return False
    except ValueError:
        return False

def findFac(a):
    b = 1
    for i in range(int(a)):
        b = b * (i + 1)
    return str(b)

theList = ""
num = input("give an integer >= 0: ")
while num != "-1":
    if isNum(num):
        theList += findFac(num) + ", "
        num = input("computed factorial. give another integer >= 0 (-1 to end): ")
    else:
        num = input("give an integer >= 0: ")
print(theList[:-2])
