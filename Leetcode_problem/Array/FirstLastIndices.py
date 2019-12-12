class Solution:
  # Time: O(n) Space: O(1)
  def getRange(self, arr, target):
    first, last = -1, -1
    for i in range(len(arr)):
      if arr[i] == target: 
        first, last = i, len(arr)-1
        for j in range(i, len(arr)-1):
          if arr[j] != arr[j+1]: last = j; break
        break
    return [first, last]
  
  # Binary Search Time: O(logn) Space: O(1) 
  def getRange2(self, arr, target):
    pivot = len(arr) // 2
    if not arr: return [-1, -1]
    if len(arr) == 1:
      return [0, 0] if arr[pivot] == target else [-1, -1]
    if arr[pivot] > target:
      return self.getRange2(arr[:pivot], target)
    elif arr[pivot] < target:
      ans = self.getRange2(arr[pivot+1:], target)
      return [pivot+1+ans[0], pivot+1+ans[1]] if ans[0] != -1 else ans
    else:
      ans1 = self.getRange2(arr[:pivot], target)
      ans2 = self.getRange2(arr[pivot+1:], target)
      first, last = -1, -1
      first = pivot if ans1[0] == -1 else ans1[0]
      last = pivot if ans2[0] == -1 else pivot + 1 + ans2[1]
      return [first, last]

# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
arr2 = [1, 2, 2, 3]
x = 8
print(Solution().getRange2(arr, x))
# [1, 4]