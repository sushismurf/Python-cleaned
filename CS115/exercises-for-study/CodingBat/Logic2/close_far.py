"""
question:

Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1),
while the other is "far", differing from both other values by 2 or more. 

my solution:
"""

def close_far(a, b, c):
  v1 = abs(a-b)
  v2 = abs(b-c)
  v3 = abs(a-c)
  if v1 < 2 and v2 >= 2 and v3 >= 2:
    return True
  elif v3 < 2 and v2 >= 2 and v1 >= 2:
    return True
  else:
    return False
