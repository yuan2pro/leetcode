/*
 * @lc app=leetcode.cn id=424 lang=java
 *
 * [424] 替换后的最长重复字符
 */

// @lc code=start
class Solution {
    public int characterReplacement(String s, int k) {
        int same = 0;
        int len = s.length();
        int left = 0, right =  0;
        int[] arr = new int[26];
        while(right < len){
            int index = s.charAt(right) - 'A';
            arr[index]++;
            same = Math.max(same, arr[index]);
            if(same + k < right - left + 1){
                arr[s.charAt(left) - 'A']-- ;
                left++;
            }
            right++;
        }
        return right - left;
    }
}
// @lc code=end

