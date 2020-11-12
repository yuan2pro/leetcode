/*
 * @lc app=leetcode.cn id=922 lang=java
 *
 * [922] 按奇偶排序数组 II
 */

// @lc code=start
class Solution {
    public int[] sortArrayByParityII(int[] A) {
        int i = 0, j = 1;
        while (true) {
            while (i < A.length && A[i] % 2 == 0)
                i += 2;
            while (j < A.length && A[j] % 2 == 1)
                j += 2;
            if (i >= A.length || j >= A.length)
                return A;
            int temp = A[i];
            A[i] = A[j];
            A[j] = temp;
        }
    }
}
// @lc code=end
