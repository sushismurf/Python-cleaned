# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:56:00 2023.

@author: doga

Take two lists and write a program that returns a list that contains only
the elements that are common between them. (no duplicates)

the solution also covers q10.
"""

L1 = []
L2 = []

print("forming list one.")

while True:
    a = input("please input a number (q to stop): ")
    if a == "q":
        break
    else:
        L1.append(a)

print("done with list one. moving on to list two.")

while True:
    a = input("please input a number (q to stop): ")
    if a == "q":
        break
    else:
        L2.append(a)

L1copy = list(L1)
L2copy = list(L2)
ab = 1
temp1 = []
temp2 = []

for i in L1copy:
    if i in L1[ab:len(L1copy)]:
        temp1.append(i)
    ab += 1

for u in temp1:
    L1.remove(u)

ab = 1

for k in L2copy:
    if k in L2[ab:len(L2copy)]:
        temp2.append(k)
    ab += 1

for o in temp2:
    L2.remove(o)

commonList = []

for t in L1:
    if t in L2 and t not in commonList:
        commonList.append(t)

for r in L2:
    if r in L1 and r not in commonList:
        commonList.append(r)

commonList.sort()
print("the numbers in common are the following: ")

for w in range(len(commonList) - 1):
    print(int(commonList[w]), end=', ')

print(int(commonList[-1]), end='')
