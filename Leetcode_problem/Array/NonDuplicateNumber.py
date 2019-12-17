# ------------Problem------------
# Given a list of numbers, where every number shows up 
# twice except for one number, find that one number.
#
# Input: [4, 3, 2, 4, 1, 3, 2]
# Output: 1


# Time: O(n) Space: O(1)
def singleNumber(nums):
  res = nums[0]
  for i in range(1, len(nums)):
    res ^= nums[i]
  return res

print(singleNumber([4, 3, 2, 4, 8, 3, 2]))
# 1