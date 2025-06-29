"""
question:

Given 3 int values, a b c, return their sum. 
However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. 
So for example, if b is 13, then both b and c do not count.

my solution:
"""

def lucky_sum(a, b, c):
  someList = [a, b, c]
  if 13 not in someList:
    return a + b + c
  else:
    i = someList.index(13)
    return sum(someList[:i])
