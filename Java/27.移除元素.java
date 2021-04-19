/*
 * @lc app=leetcode.cn id=27 lang=java
 *
 * [27] 移除元素
 */

// @lc code=start
class Solution {
    public int removeElement(int[] nums, int val) {
        int first = 0, last = nums.length - 1;
        int modNum = 0;
        while (first <= last) {
            if (nums[first] == val) {
                if (nums[last] != val) {
                    int t = nums[first];
                    nums[first] = nums[last];
                    nums[last] = t;
                    first++;
                    last--;
                    modNum++;
                } else {
                    last--;
                    modNum++;
                }
            } else {
                first++;
            }
        }
        return nums.length - modNum;
    }
}
// @lc code=end
