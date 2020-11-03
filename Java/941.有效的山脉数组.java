/*
 * @lc app=leetcode.cn id=941 lang=java
 *
 * [941] 有效的山脉数组
 */

// @lc code=start
class Solution {
    public boolean validMountainArray(int[] A) {
        if (A == null || A.length < 3)
            return false;
        int i = 0, j = A.length - 1;
        int step = 0;
        while (i < j) {
            if (A[i + 1] > A[i])
                i++;
            if (A[j - 1] > A[j])
                j--;
            step++;
            if (step == A.length) {
                return false;
            }
        }
        if (i == 0 || j == A.length - 1) {
            return false;
        }
        return true;
    }
}
// @lc code=end
