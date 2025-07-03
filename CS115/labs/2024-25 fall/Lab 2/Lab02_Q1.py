#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 07:46:44 2024

"""

# a. Use a for loop to calculate and display the first 10 powers of 5
num = 5
N = 10
print(f'The first {N} powers of {num}: ', end='')
print(f'{num ** 0}', end='')
for i in range(1, N):
    print(f', {num ** i}', end='')
print()


# b. Use a while loop to find the powers of 5 in the specified range
lower_bound = int(input('Enter lower bound: '))
upper_bound = int(input('Enter upper bound: '))

print(f'Powers of 5 between {lower_bound} and {upper_bound}: ')

power = 0
while num ** power <= upper_bound:
    if num ** power >= lower_bound:
        print(f'{num} ** {power}  is {num**power}')    
    power += 1
