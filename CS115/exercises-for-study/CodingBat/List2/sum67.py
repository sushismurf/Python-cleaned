"""
question:

Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 and extending to the next 7 
(every 6 will be followed by at least one 7). Return 0 for no numbers.

my solution:
"""

def sum67(nums):
  count = 0
  skip = False
  for i in nums:
    if i != 6 and skip == False:
      count += i
    elif i == 6:
      skip = True
    elif i == 7:
      skip = False
  return count
