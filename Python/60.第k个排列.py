#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
import itertools


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]
        total = 1
        for p in itertools.permutations(nums, n):
            if total == k:
                return "".join(p)
            total += 1


# @lc code=end
