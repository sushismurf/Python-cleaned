"""
question:

Given 2 ints, a and b, return their sum. 
However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

my solution:
"""

def sorta_sum(a, b):
  if 10 <=  a + b <= 19:
    return 20
  else:
    return a + b
