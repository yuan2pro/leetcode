# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 10:08
# @Author  : ProYuan
"""
三数之和
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 存储结果列表
        res_list = []
        # 对nums列表进行排序，无返回值，排序直接改变nums顺序
        nums.sort()
        for i in range(len(nums)):
            # 如果排序后第一个数都大于0，则跳出循环，不可能有为0的三数之和
            if nums[i] > 0:
                break
            # 排序后相邻两数如果相等，则跳出当前循环继续下一次循环，相同的数只需要计算一次
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 记录i的下一个位置
            j = i + 1
            # 最后一个元素的位置
            k = len(nums) - 1
            while j < k:
                # 判断三数之和是否为0
                if nums[j] + nums[k] == -nums[i]:
                    # 把结果加入数组中
                    res_list.append([nums[i], nums[j], nums[k]])
                    # 判断j相邻元素是否相等，有的话跳过这个
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    # 判断后面k的相邻元素是否相等，是的话跳过
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    # 没有相等则j+1，k-1，缩小范围
                    j += 1
                    k -= 1
                # 小于-nums[i]的话还能往后取
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return res_list

    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tmp = dict()
        for i in range(len(nums)):
            tmp[nums[i]] = tmp.get(nums[i], 0) + 1
        left = sorted(filter(lambda x: x < 0, tmp))
        right = sorted(filter(lambda x: x >= 0, tmp))
        if 0 in tmp and tmp[0] > 2:
            res = [[0, 0, 0]]
        else:
            res = []
        for i in left:
            for j in right:
                mid = -i - j
                if mid in tmp:
                    if mid in (i, j) and tmp[mid] > 1:
                        res.append([i, mid, j])
                    elif mid < i or mid > j:
                        res.append([i, mid, j])
        return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
