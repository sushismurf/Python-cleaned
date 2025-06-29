"""
question:

Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

my solution:
"""

def makes10(a, b): 
  if a+b == 10: 
    return True
  elif a == 10 or b == 10: 
    return True
  else: 
    return False
