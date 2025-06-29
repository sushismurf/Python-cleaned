"""
question:

Return the number of times that the string "hi" appears anywhere in the given string.

my solution:
it doesn't make sense that 'Hi', 'hI' etc doesn't count towards the answer.
the code below just searches for 'hi'
"""

def count_hi(s):
  count = 0
  for i in range(len(s)-1):
    if s[i] == 'h' and i != len(s):
      if s[i+1] == 'i':
        count += 1
  return count
