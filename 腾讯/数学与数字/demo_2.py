#!/usr/bin/env python
# encoding: utf-8
# @time: 2018-12-11 21:45
# @author: ProYuan
# @Software: PyCharm
"""
回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1] == str(x)

    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ##不使用字符串
        if x < 0:
            return False
        ReverseNum = 0
        OrignNum = x
        while (OrignNum):
            ReverseNum = ReverseNum * 10
            ReverseNum = ReverseNum + OrignNum % 10
            OrignNum = OrignNum // 10
        return x == ReverseNum


if __name__ == '__main__':
    x = 12121
    print(Solution().isPalindrome1(x))
