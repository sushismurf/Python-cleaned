"""
question:

Given 2 arrays of ints, a and b, return True if they have the same first element
or they have the same last element. 
Both arrays will be length 1 or more.

my solution:
"""

def common_end(a, b):
  if a[-1] == b[-1] or a[0] == b[0]:
    return True
  else:
    return False
