"""
question:

Given a string, return a version without the first and last char, 
so "Hello" yields "ell". The string length will be at least 2.

my solution:
"""

def without_end(s):
  return s[1:-1]
