# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 15:58
# @Author  : ProYuan
# @File    : demo_3.py

"""
最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Manacher's Algorithm
        # 添加#
        if len(s) < 2 or s == s[::-1]:
            return s
        # 中心拓展算法
        max_len = 1  # 回文子串长度
        start = 0  # 回文子串起始位置
        for i in range(1, len(s)):
            even = s[i - max_len: i + 1]  # 偶数回文子串
            odd = s[i - max_len - 1: i + 1]  # 奇数回文子串
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
        return s[start: start + max_len]


if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))
