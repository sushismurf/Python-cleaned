# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:28:12 2024.

q: Write a program which accepts a sequence of words separated by whitespace
as input to print the words composed of digits only.

Example:
If the following words is given as input to the program:

2 cats and 3 dogs.

Then, the output of the program should be:

['2', '3']

In case of input data being supplied to the question, it should be assumed
to be a console input.

@author: sushismurf
"""

while True:
    a = input("give whitespace seperated words (0000 to quit): ")
    if a == '0000':
        break
    for i in range(len(a)):
        if a[i].isdigit() or a[i].isalpha() or a[i].isspace():
            pass
        elif i == len(a):
            break
        else:
            print("that doesnt seem like a word..")
            break
    b = str()
    for j in a:
        if j.isdigit() or j.isspace():
            b += j
    b = b.split()
    print(b)
print("bye!")
