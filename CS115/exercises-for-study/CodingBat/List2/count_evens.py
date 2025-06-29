"""
question:

Return the number of even ints in the given array.

my solution:
"""

def count_evens(nums):
  count = 0
  for i in nums:
    if i % 2 == 0:
      count += 1
  return count
