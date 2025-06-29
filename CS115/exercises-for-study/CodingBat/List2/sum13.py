"""
question:

Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

my solution:
"""

def sum13(nums):
  if len(nums) == 0:
    return 0
  else:
    count = 0
    skip = False
    for i in nums:
      if i == 13:
        skip = True
      elif skip:
        skip = False
      else:
        count += i
    return count
