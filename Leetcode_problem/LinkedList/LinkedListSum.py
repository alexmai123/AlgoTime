# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # base case checking
    res = ListNode(0)
    if not l1 and not l2: return res
    elif not l1: return l2
    elif not l2: return l1
    else:
      curr1, curr2, curr3, prev = l1, l2, res, res
      # loop through until one linked list out
      while curr1 and curr2:
        c, curr3.val = self.add(curr1.val, curr2.val, c)
        curr3.next = ListNode(0)
        prev = curr3
        curr3 = curr3.next
        curr1 = curr1.next
        curr2 = curr2.next
      # after one linked list runs out continue on the remaining one
      # case1: both runs out
      if not curr1 and not curr2:
        prev.next = None if c==0 else ListNode(c)
        return res
      elif not curr1:
        while curr2:
          c, curr3.val = self.add(0, curr2.val, c)
          curr3.next = ListNode(0)
          prev = curr3
          curr3 = curr3.next
          curr2 = curr2.next
      else:
        while curr1:
          c, curr3.val = self.add(curr1.val, 0, c)
          curr3.next = ListNode(0)
          prev = curr3
          curr3 = curr3.next
          curr1 = curr1.next
      prev.next = None if c==0 else ListNode(c)
      return res
    
  def add(self, n1, n2, c):
    res = n1 + n2 + c
    return res // 10, res % 10

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(5)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8