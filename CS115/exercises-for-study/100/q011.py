# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:45:42 2024.

q: Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated
sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010

@author: billypatty
"""

def seq():
    flag = 0
    while True:
        a = input("give a 4-digit binary number(s) seperated with commas"
                  " (example: 0000,0010,0110): ")
        for i in a:
            if i == '0' or i == '1' or i == ',':
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
nums = seq()
out = []
for i in nums:
    if ((int(i[0])*8 + int(i[1])*4 + int(i[2])*2 + int(i[3])) % 5 == 0
       and i != "0000"):
        out.append(i)
print(','.join(out))
