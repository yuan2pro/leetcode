#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
import itertools


class Solution:
    def combine(self, n: int, k: int):
        nums = [i for i in range(1, n + 1)]
        ans = []
        for p in itertools.combinations(nums, k):
            ans.append(list(p))
        return ans


# @lc code=end
