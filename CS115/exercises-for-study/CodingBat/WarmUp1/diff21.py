"""
question:

Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

my solution:
"""

def diff21(a):
  if a<=21:
    return abs(a-21) 
  else: # other cases 
    return 2*abs(a-21)
