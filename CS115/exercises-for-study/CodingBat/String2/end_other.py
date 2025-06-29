"""
question:

Given two strings, return True if either of the strings appears at the very end of the other string, 
ignoring upper/lower case differences.

my solution:
"""

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return a.endswith(b) or b.endswith(a)
