// Leetcode 198
// ---------------------Description-----------------------------
// You are a professional robber planning to rob houses along a street.
// Each house has a certain amount of money stashed, the only constraint
// stopping you from robbing each of them is that adjacent houses 
// have security system connected and it will automatically contact 
// the police if two adjacent houses were broken into on the same night.

// Given a list of non-negative integers representing the amount of 
// money of each house, determine the maximum amount of money you can 
// rob tonight without alerting the police.

// ---------------------Example----------------------------
// Input: [1, 3, 2, 4]
// Ouput: 7

class HouseRob {
  int rob(int[] nums) {
    if (nums.length == 0) {
      return 0;
    }
    if (nums.length == 1) {
      return nums[0];
    }
    int[] dp = new int[nums.length];
    dp[0] = nums[0];
    dp[1] = Math.max(dp[0], nums[1]);
    for (int i = 2; i < nums.length; i++) {
      dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
    }
    return dp[nums.length - 1];
  }

  public static void main(String args[]) {
    int[] input = { 1, 3, 2, 4 };
    int output = 7;
    HouseRob a = new HouseRob();
    System.out.println("Your result is " + a.rob(input));
    System.out.println("Actual result is " + output);

  }
}

