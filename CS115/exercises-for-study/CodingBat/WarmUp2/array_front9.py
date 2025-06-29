"""
question:

Given an array of ints, return True if one of the first 4 elements in the array is a 9.
The array length may be less than 4.

my solution:
"""

def array_front9(nums):
  if len(nums) < 4:
    for i in range(len(nums)):
      if nums[i] == 9:
        return True
    else:
      return False
  else:
    for i in range(0,4):
      if nums[i] == 9:
        return True
    else:
      return False
