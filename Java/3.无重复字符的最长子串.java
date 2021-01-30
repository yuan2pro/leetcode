/*
 * @lc app=leetcode.cn id=3 lang=java
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0 || "".equals(s)){
            return 0;
        }
        Map<Character, Integer> map = new HashMap<>();
        char[] chars = s.toCharArray();
        int start = 0;
        int maxLen = 0;
        for(int i = 0;i < chars.length; i++){
            if(map.containsKey(chars[i])){
                start = Math.max(start, map.get(chars[i])+1);
            }
            map.put(chars[i], i);
            maxLen = Math.max(maxLen, i + 1 - start);
        }
        return maxLen;
    }
}
// @lc code=end

