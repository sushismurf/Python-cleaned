# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:19:00 2024.

q: Write a program that accepts a comma separated
sequence of words as input and prints the words in a
comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

@author: doga
"""

def seq():
    flag = 0
    while True:
        a = input("give a comma-separated sequence of words"
                  " (example: hello,hi,hey): ")
        for i in a:
            if i.isalpha() or i == ',':
                pass
            else:
                flag = 1
                print('invalid input.')
                break
        if flag == 0:
            d = a.split(',')
            return d
        else:
            flag = 0
words = seq()
lowerWords = []
for i in words:
    lowerWords.append(i.lower())
lowerWords.sort()
for j in words:
    for k in range(len(lowerWords)):
        if j.lower() == lowerWords[k]:
            lowerWords[k] = j
            break
print(','.join(lowerWords))
