# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:56:31 2024.

q: Write a program that accepts a sequence of whitespace
separated words as input and prints the words after removing all
duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

@author: doga
"""

def seq():
    flag = 0
    while True:
        a = input("give a sentence (no punctuation!!): ")
        for i in a:
            if i.isalpha() or i.isspace():
                pass
            else:
                flag = 1
                print('invalid input.')
                break
        if flag == 0:
            d = a.split(' ')
            return d
        else:
            flag = 0
sentenceSeperated = seq()
lowerSentence = []
for i in sentenceSeperated:
    lowerSentence.append(i.lower())
lowerSentence.sort()
for j in sentenceSeperated:
    for k in range(len(lowerSentence)):
        if j.lower() == lowerSentence[k]:
            lowerSentence[k] = j
            break
print(' '.join(lowerSentence))
