# ---------------Problem--------------
# Given a list of numbers with only 3 unique numbers (1, 2, 3), 
# sort the list in O(n) time. Can you do this in constant space?
# Example 1:
# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]

#Time: O(n) Space: O(1)
def sortNums(nums):
  d = {1:0, 2:0, 3:0}
  for num in nums:
    if num not in d: d[num] = 1
    else: d[num] += 1
  return [1]*d[1] + [2]*d[2] + [3]*d[3]

  

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]