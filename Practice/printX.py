# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:33:49 2023.

@author: doga

Replace the comment in the following code with a
while loop.
num_x = int(input('How many times should I print the letter
X? '))
to_print = ''
#concatenate X to to_print num_x times
print(to_print)

"""

num_x = int(input('How many times should I print the letter X?: '))
to_print = ''

if num_x < 0:
    print("i cant print something negative times.")

numPrinted = 0

while numPrinted < num_x:
    to_print += "x"
    numPrinted += 1

print(to_print)
