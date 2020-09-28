#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        if l % 2 != 0:
            return False
        if s[0: l // 2] == s[l // 2:]:
            return True
        else:
            return False


# @lc code=end
