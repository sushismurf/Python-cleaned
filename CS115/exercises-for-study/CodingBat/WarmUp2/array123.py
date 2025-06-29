"""
question:

Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

my solution:
"""
def array123(nums):
  if len(nums)<3:
    return  False
  else:
    for i in range(len(nums)-2):
      if nums[i] == 1:
        if nums[i+1] == 2:
          if nums[i+2] == 3:
            return True
    return False
