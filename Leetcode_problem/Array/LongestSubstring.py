class Solution:
  def lengthOfLongestSubstring(self, s):
    d = {}
    maxlen = 0
    curr_len = 0
    prev_idx = 0
    for i in range(len(s)):
      if s[i] not in d:
        d[s[i]] = i
        curr_len += 1
      else:
        if d[s[i]] < prev_idx:
          d[s[i]] = i
          curr_len += 1
        else:
          curr_len -= d[s[i]] - prev_idx
          prev_idx = d[s[i]] + 1
          d[s[i]] = i
      maxlen = max(maxlen, curr_len)
    return maxlen
        
      


print(Solution().lengthOfLongestSubstring("aaaaaaa"))
# 10
