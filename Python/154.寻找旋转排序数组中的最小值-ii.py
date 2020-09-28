#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            privor = low + (high - low) // 2
            if nums[privor] > nums[high]:
                low = privor + 1
            elif nums[privor] < nums[high]:
                high = privor
            else:
                high -= 1
        return nums[low]

# @lc code=end

