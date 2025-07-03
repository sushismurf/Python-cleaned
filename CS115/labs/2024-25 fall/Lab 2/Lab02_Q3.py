#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:19:10 2024

"""

lower_bound = int(input('Enter lower bound: '))
upper_bound = int(input('Enter upper bound: '))

while lower_bound != 0 or upper_bound != 0:
    total = 0
    count = 0
    if lower_bound < upper_bound:
        for i in range(lower_bound, upper_bound + 1):
            if i % 7 == 0 and i % 5 != 0:
                total += i
                count += 1

        if count != 0:
            avg = total / count
            print(count, 'values are divisible by 7 but not 5 between', 
                  lower_bound, 'and', upper_bound, ', inclusive')
            print('Average of those values: ', avg)
        else:
            print('No values found')
    else:
        print('Invalid range')
    lower_bound = int(input('Enter lower bound: '))
    upper_bound = int(input('Enter upper bound: '))


print('bye!')