import java.util.Deque;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.TreeSet;

/*
 * @lc app=leetcode.cn id=220 lang=java
 *
 * [220] 存在重复元素 III
 */

// @lc code=start
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeSet<Long> treeSet = new TreeSet<>();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            Long ceiLong = treeSet.ceiling((long) nums[i] - (long) t);
            if (ceiLong != null && ceiLong <= (long) nums[i] + t) {
                return true;
            }
            treeSet.add((long) nums[i]);
            if (i >= k) {
                treeSet.remove((long) nums[i - k]);
            }
        }
        return false;
    }
}
// @lc code=end
