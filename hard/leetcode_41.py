'''
41. 缺失的第一个正数
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。



示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
'''


class Solution:
    def firstMissingPositive(self, nums):
        # nums.sort()
        a = max(nums)
        if a < 0: return 1
        for i in range(1, a+2):
            if i not in nums:
                return i

print(Solution().firstMissingPositive([]))