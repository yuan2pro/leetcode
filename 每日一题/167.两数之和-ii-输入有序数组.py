#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#


# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            x = target - numbers[i]
            j = self.div(numbers, x, i+1)
            if j == -1:
                continue
            else:
                break
        return [i + 1, j + 1]

    def div(self, nums, target, lo=0, hi=None):
        if lo < 0:
            return -1
        if hi is None:
            hi = len(nums)-1
        while (lo <= hi):
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
        return -1


# @lc code=end
