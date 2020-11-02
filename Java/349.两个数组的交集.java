/*
 * @lc app=leetcode.cn id=349 lang=java
 *
 * [349] 两个数组的交集
 */

// @lc code=start
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        if (nums1.length < nums2.length) {
            intersection(nums2, nums1);
        }
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nums2.length; i++) {
            set.add(nums2[i]);
        }
        Set<Integer> set1 = new HashSet<>();
        for (int i = 0; i < nums1.length; i++) {
            if (set.contains(nums1[i])) {
                set1.add(nums1[i]);
            }
        }
        int[] ans = new int[set1.size()];
        int i = 0;
        for (Integer integer : set1) {
            ans[i++] = integer;
        }
        return ans;
    }
}
// @lc code=end
