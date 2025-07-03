# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:58:02 2024.

q: Please write a program which count and print the numbers of each character
in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

@author: doga
"""

a = input("say somethin': ")
b = dict()
for i in a:
    if i not in b:
        b[i] = 1
    else:
        b[i] += 1
c = list(dict.items(b))
for j in range(len(c)):
    print(c[j])
