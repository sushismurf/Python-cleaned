"""
question:

Return True if the string "cat" and "dog" appear the same number of times in the given string.

my solution:
"""

def cat_dog(s):
  c = s.count('cat')
  d = s.count('dog')
  return c == d
