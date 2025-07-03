#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:31:32 2024

"""

name1 = input('Enter the first name: ')
name2 = input('Enter the second name: ')
name3 = input('Enter the third name: ')


if name1 <= name2 and name1 <= name3:
    first = name1
elif name2 <= name1 and name2 <= name3:
    first = name2
else:
    first = name3
    
print(f'{first} comes first in lexicographic ordering.')    

# # alternative solution
# if name1 > name2:
#     name1, name2 = name2, name1

# if name1 > name3:
#     name1, name3 = name3, name2

# if name1 > name2:
#     name1, name2 = name2, name1

# print(f'{name1} comes first in lexicographic ordering.')    