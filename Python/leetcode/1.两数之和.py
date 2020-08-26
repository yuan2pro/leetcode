#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        d = {}
        for i in range(len(nums)):
            d[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in d.keys() and i != d[nums[i]]:
                if i > d[nums[i]]:
                    ans = [d[nums[i]], i]
                else:
                    ans = [i, d[nums[i]]]
                break
        return ans

# @lc code=end
