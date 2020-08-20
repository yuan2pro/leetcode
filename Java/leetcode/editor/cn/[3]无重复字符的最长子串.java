package leetcode.editor.cn;
//给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
//
// 示例 1: 
//
// 输入: "abcabcbb"
//输出: 3 
//解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
// 
//
// 示例 2: 
//
// 输入: "bbbbb"
//输出: 1
//解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
// 
//
// 示例 3: 
//
// 输入: "pwwkew"
//输出: 3
//解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
//     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
// 
// Related Topics 哈希表 双指针 字符串 Sliding Window 
// 👍 4191 👎 0


import java.util.HashMap;
import java.util.Map;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution3 {
    public int lengthOfLongestSubstring(String s) {
        if ("".equals(s) || s.length() == 0) {
            return 0;
        }
        if (s.length() == 1) {
            return 1;
        }
        Map<Character, Integer> map = new HashMap<>();
        char[] chars = s.toCharArray();
        int len = chars.length;
        int res = 0;
        int tmp = 0;
        for (int i = 0; i < len; i++) {
            if (map.containsKey(chars[i])) {
                Integer index = map.get(chars[i]);
                tmp = Math.max(tmp, index + 1);
            }
            map.put(chars[i], i);
            res = Math.max(res, i - tmp + 1);
        }
        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
