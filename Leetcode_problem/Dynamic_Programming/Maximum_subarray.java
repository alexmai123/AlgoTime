// Leetcode 53
// ---------------------Description--------------------------
// Given an integer array nums, find the contiguous subarray 
// (containing at least one number) which has the largest sum
//  and return its sum.

// ---------------------Example------------------------------
// Input: [-2,1,-3,4,-1,2,1,-5,4],
// Output: 6

class MS {
  public int maxSubArray(int[] nums) {
      int[] dp = new int[nums.length];
      dp[0] = nums[0];
      int max = dp[0];
      for (int i=1; i<nums.length; i++){
          dp[i] = Math.max(dp[i-1]+nums[i], nums[i]);
          max = Math.max(dp[i], max);
      }
      return max;  
  }

  public static void main(String args[]){
    int[] input = {-2,1,-3,4,-1,2,1,-5,4};
    int output = 6;
    MS a = new MS();
    System.out.println("Your result is " + a.maxSubArray(input));
    System.out.println("Actual result is " + output);
  }
}