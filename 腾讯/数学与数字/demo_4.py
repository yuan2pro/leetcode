#!/usr/bin/env python
# encoding: utf-8
# @time: 2018-12-11 21:49
# @author: ProYuan
# @Software: PyCharm
"""
求众数
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
"""
from collections import Counter


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return Counter(nums).most_common(1)[0][0]

    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        temp = None
        for i in nums:
            if count == 0:
                temp = i
            count += 1 if i == temp else -1
        return temp


if __name__ == '__main__':
    nums = [2,2,1,1,1,2,2]
    print(Solution().majorityElement1(nums))
