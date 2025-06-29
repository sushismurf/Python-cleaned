"""
question:

Given a string, return a string where for every char in the original, there are two chars.

my solution:
"""

def double_char(s):
  newDouble = ''
  for i in s:
    newDouble += 2*i
  return newDouble
