# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:26:00 2024.

q: Write a program which takes 2 digits, X,Y as input and generates a
2-dimensional array. The element value in the i-th row and j-th column
of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

@author: doga
"""

def twoNums():
    flag = 0
    while True:
        a = input("give two comma-separated integers"
                  " (example: 1,2): ")
        for i in a:
            if i.isdigit() or i == ',':
                pass
            else:
                flag = 1
                break
        if flag == 0 and len(a) == 3:
            d = a.split(',')
            return d
        else:
            flag = 0
            print('invalid input')
nums = twoNums()
rows = int(nums[0])
cols = int(nums[1])
mats = []
helper = []
for i in range(rows):
    for j in range(cols):
        helper.append(i*j)
    mats.append(helper)
    helper = []
print(mats)
