p_map = {'(': ')', '[': ']', '{': '}'}

class Solution:
  # Recursion Time: O(n^3) Space: O(1)
  def isValid1(self, s):
    global p_map
    if not s: return True
    elif len(s) == 1: return False
    else:
      for i in range(len(s)):
        if s[i] not in p_map: return False
        else:
          for j in range(len(s)):
            if s[j] == p_map[s[i]]:
              return self.isValid1(s[i+1: j]) and self.isValid1(s[j+1:])
          return False

  # Stack(FILO) Time: O(n) Space: O(n)
  def isValid2(self, s):
    global p_map
    stack = []
    for i in range(len(s)):
      # push into the stack that the closing one we want
      if s[i] in p_map:
        stack.append(p_map[s[i]])
      else:
        if not stack: return False
        elif stack.pop() != s[i]: return False
    return not stack


# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid2(s))

s = ""
# should return True
print(Solution().isValid2(s))

s = "([{}])()"
# should return True
print(Solution().isValid2(s))