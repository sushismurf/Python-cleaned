# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:13:02 2023.

@author: billypatty

Write a program that prints the sum of the prime
numbers greater than 2 and less than 1000. Hint: you probably want
to use a for loop that is a primality test nested inside a for loop that
iterates over the odd integers between 3 and 999.
"""

sumValue = 0

for i in range(3, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
        elif i == j + 1:
            sumValue += i
        elif not i % j == 0 and j < i:
            continue

print(sumValue + 2)
