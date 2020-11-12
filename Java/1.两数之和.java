/*
 * @lc app=leetcode.cn id=1 lang=java
 *
 * [1] 两数之和
 */

// @lc code=start
import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                int left = map.get(nums[i]);
                return new int[] { left, i };
            } else {
                map.put(target - nums[i], i);
            }
        }
        return null;
    }
}
// @lc code=end
