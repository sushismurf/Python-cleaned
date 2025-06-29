"""
question:

Given 2 strings, a and b, return a string of the form short+long+short, 
with the shorter string on the outside and the longer string on the inside. 
The strings will not be the same length, but they may be empty (length 0).

my solution:
the question doesn't seem to care about a and b having the same length for some reason. 
so my solution won't either.
"""

def combo_string(a, b):
  if len(a) < len(b):
    return a + b + a
  else:
    return b + a + b
