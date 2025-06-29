"""
question:

Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

my solution:
i solved this using a longer path, and compared the length of each word. maybe you can think of a shorter answer?
"""

def string_match(a, b):
  if len(a) == len(b):
    count = 0
    for i in range(len(a)-1):
      if a[i] == b[i]:
        if a[i+1] == b[i+1]:
          c = a[i] + a[i+1]
          count += 1
    return count
  elif len(a) < len(b):
    count = 0
    for i in range(len(a)-1):
      if a[i] == b[i]:
        if a[i+1] == b[i+1]:
          c = a[i] + a[i+1]
          count += 1
    return count
  else:
    count = 0
    for i in range(len(b)-1):
      if a[i] == b[i]:
        if a[i+1] == b[i+1]:
          c = a[i] + a[i+1]
          count += 1
    return count
