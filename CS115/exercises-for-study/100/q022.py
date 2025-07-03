# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 12:32:46 2024.

q: Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or
Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

@author: doga
"""

n = {}
a = input("give a sentence: ").strip()
words = a.split()
for i in words:
    n[i] = n.get(i, 0)+1
words = sorted(n.keys())
for j in words:
    print(j, ':', n[j])
