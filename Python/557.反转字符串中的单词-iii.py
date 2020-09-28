#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start


class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        for i in range(len(a)):
            a[i] = a[i][::-1]
        return " ".join(a)

# @lc code=end
