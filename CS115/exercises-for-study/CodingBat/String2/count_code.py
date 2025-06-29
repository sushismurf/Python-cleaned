"""
question:

Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count.

my solution:
"""

def count_code(s):
  count = 0
  for i in range(len(s) - 3):
    if s[i:i+2] == 'co' and s[i+3] == 'e':
      count += 1
  return count
