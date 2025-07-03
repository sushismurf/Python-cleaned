# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:09:18 2024.

q: Use a list comprehension to square each odd number in a list.
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

@author: doga
"""

def seq():
    flag = 0
    while True:
        a = input("give comma-separated integers"
                  " (example: 1,2): ")
        for i in a:
            if i.isdigit() or i == ',':
                pass
            else:
                flag = 1
                break
        if flag == 0:
            d = a.split(',')
            return d
        else:
            flag = 0
            print('invalid input')
nums = seq()
outList = []
for i in nums:
    if int(i) % 2 == 1:
        outList.append(i)
print(','.join(outList))
