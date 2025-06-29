# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:37:54 2024.

q: Write a program that accepts sequence of lines as input and
prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

@author: billypatty
"""

def seq():
    while True:
        a = input("give a word or sentence ('q' to quit): ")
        if a.lower() == 'q':
            print('bye!')
            break
        else:
            print(a.upper())
seq()
