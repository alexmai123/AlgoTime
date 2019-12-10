class Solution:
  def lengthOfLongestPalindrome(self, s):
    # manacher algorithm
    T = '#'.join('${}@'.format(s))
    n = len(T)
    print(T)
    res = [0] * n
    C = R = 0
    for i in range(1, n-1):
      res[i] = (R>i) and min(R-i, res[2*C-i])
      while T[i + 1 + res[i]] == T[i - 1 - res[i]]:
        res[i]+=1

      if i + res[i] > R: 
        C, R = i, i+res[i]
    return max(res)


if __name__ == "__main__":
  print(Solution().lengthOfLongestPalindrome('abcdcccba'))
