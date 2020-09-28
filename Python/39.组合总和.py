#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start

import collections


class Solution:
    def combinationSum(self, candidates, target: int):
        ans = []
        minnum = min(candidates)
        candidates.sort()
        deque = collections.deque()

        def backtrack(candidates, begin, end, target, deque):
            if target < 0:
                return
            if target == 0:
                ans.append(list(deque))
                return
            for i in range(begin, end):
                if (target - candidates[i] < 0):
                    break
                deque.append(candidates[i])
                backtrack(candidates, i, end,
                          target - candidates[i], deque)
                deque.pop()
        backtrack(candidates, 0, len(candidates), target, deque)
        return ans


# @lc code=end
