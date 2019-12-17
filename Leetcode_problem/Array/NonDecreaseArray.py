# ------------Problem----------------
# You are given an array of integers in an arbitrary order. 
# Return whether or not it is possible to make the array 
# non-decreasing by modifying at most 1 element to any value.
# We define an array is non-decreasing if array[i] <= array[i + 1]
# holds for every i (1 <= i < n).
# 
# Input: [13, 4, 7] 
# Ouput: True
# Input: [5, 1, 3, 2, 6] 
# Ouput: False

def check(A):
  p = None
  for i in range(len(A) - 1):
      if A[i] > A[i+1]:
          if p is not None:
              return False
          p = i

  return (p is None or p == 0 or p == len(A)-2 or
          A[p-1] <= A[p+1] or A[p] <= A[p+2])


print(check([13, 4, 7]))
# True
print(check([5,6,3,4,5]))
# False
