#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import collections


class Solution:
    def topKFrequent(self, nums, k: int):
        c = collections.Counter(nums)
        data = sorted(c.items(), key=lambda x: -x[1])
        ans = []
        for i in range(k):
            ans.append(data[i][0])
        return ans

# @lc code=end
