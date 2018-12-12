# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 15:03
# @Author  : ProYuan
# @File    : demo1.py
"""
两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            if ans.count(i) == 0:
                a = target - nums[i]
                try:
                    b = nums.index(a)
                    if i != b:
                        ans.extend([i, b])
                except Exception as e:
                    continue
        return ans

    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        d = {}
        for i in range(n):
            a = target - nums[i]
            if nums[i] in d:
                return d[nums[i]], i
            else:
                d[a] = i


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum1(nums, target))
