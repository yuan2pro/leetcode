#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l = len(s)
        ans, last, i = 0, 0, 0
        while i < l:
            count = 0
            cur = s[i]
            while i < l and s[i] == cur:
                i += 1
                count += 1
            ans += min(count, last)
            last = count
        return ans
                    
                
                
# @lc code=end

