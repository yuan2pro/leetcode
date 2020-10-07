#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start


class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        m = dict()
        for num in nums:
            m[num] = m.get(num, 0) + 1
        a = m.get(0, 0)
        b = m.get(1, 0)
        c = m.get(2, 0)
        nums[:a] = [0 for _ in range(a)]
        nums[a: a + b] = [1 for _ in range(b)]
        nums[a + b:] = [2 for _ in range(c)]

# @lc code=end
