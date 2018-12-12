#!/usr/bin/env python
# encoding: utf-8
# @time: 2018-12-11 21:36
# @author: ProYuan
# @Software: PyCharm
"""
整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = list(str(x))
        if x >= 0:
            ans = int("".join(l[::-1]))
        else:
            ans = -int("".join(l[:0:-1]))
        if ans < -2 ** 31 or ans > 2 ** 31 - 1:
            return 0
        return ans

    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 2 ** 31 - 1 and x >= -2 ** 31:
            strx = str(x)[::-1]
            if strx[-1] == '-': strx = '-' + strx[:-1]
            if int(strx) <= 2 ** 31 - 1 and int(strx) >= -2 ** 31:
                return int(strx)
            else:
                return 0
        else:
            return 0


if __name__ == '__main__':
    print(Solution().reverse(0))
