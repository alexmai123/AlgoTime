class Solution: 
    # Time: O(n^2) Space: O(1)
    def longestPalindrome1(self, s):
      T = '#'.join('${}@'.format(s))
      max_len = 0
      max_pos = 0
      for i in range(1, len(T)-1):
        j = 1
        curr_len = 1
        while i - j >= 0 and i + j < len(T):
          if T[i-j] == T[i+j]:
            curr_len+=1
          j+=1
        if max_len < curr_len:
          max_len = curr_len
          max_pos = i
      start = max_pos - max_len
      return s[start:start+max_len]
    
    # Manacher Algo Time: O(n) Space: O(n)
    def longestPalindrome2(self, s):
      T = '#'.join('${}@'.format(s))
      P = [0] * len(T)
      C, R = 1, 1
      for i in range(1, len(T)-1):
        # curr position is out of right bound therefore no infomation is gurantee
        if (R < i): P[i] = 0
        # Can retrieve infomation from mirr pos
        else:
          P[i] = min(R-i, 2*C-i)
        while T[C-P[i]-1] == T[C+P[i]+1]: P[i] += 1
        # update the center pos and right bound
        if R < i:
          C = i
          R = i + P[i]
      maxlen = max(P)
      start = P.index(maxlen)//2-1 - maxlen//2
      return s[start:start+maxlen]

# Test program
s = "tracecars"
print(str(Solution().longestPalindrome2(s)))
# racecar