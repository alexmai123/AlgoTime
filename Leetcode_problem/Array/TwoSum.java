import java.util.*;

// -------------------- LeetCode Q1 -------------------------
// Given an array of integers, return indices of the two numbers 
// such that they add up to a specific target.
// You may assume that each input would have exactly one solution, 
// and you may not use the same element twice.
// Example: 
// Input: nums = [2, 5, 6, 8] target: 11 
// Output: [1, 2] (nums[1] + nums[2] = 11)

class Solution {
  // Time: O(n^2) Space: O(1)
  public int[] twoSum1(int[] nums, int target) {
    // simply loop through one then check the rest 
    for (int i=0; i<nums.length; i++){
      for (int j=i; j<nums.length; j++){
        if (nums[i] + nums[j] == target){
          return new int[] {i, j};
        }
      }
    }
    throw new IllegalArgumentException("No Solution");
  }

  // Time: O(n) Space: O(n)
  public int[] twoSum2(int[] nums, int target){
    // using hashmap to store therefore look up will be O(1)
    Map<Integer, Integer> numMap = new HashMap<Integer, Integer>();
    for (int i=0; i<nums.length; i++){
      int complement = target - nums[i];
      if (numMap.containsKey(complement)){
        return new int[] { numMap.get(complement), i};
      }
      numMap.put(nums[i], i);
    }
    throw new IllegalArgumentException("No Solution");
  }

  public static void main(String[] args) {
    int[] nums = {2,7,11,15};
    int target = 13;
    Solution c = new Solution();
    int[] res = c.twoSum2(nums, target);
    System.out.printf("%d %d", res[0], res[1]); 
  }
}