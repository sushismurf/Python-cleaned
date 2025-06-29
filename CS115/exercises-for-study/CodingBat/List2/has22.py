"""
question:

Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

my solution:
"""

def has22(nums):
  is2 = False
  for i in nums:
    if i != 2:
      is2 = False
    elif i == 2 and is2 == False:
      is2 = True
    elif i == 2 and is2 == True:
      return True
    else:
      return -1
  return False
