#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start

import collections


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        deque = collections.deque()
        ans = []

        def backtrack(candidates, start, end, target, deque):
            if target < 0:
                return
            if target == 0:
                if list(deque) not in ans:
                    ans.append(list(deque))
                return
            for i in range(start, end):
                if target - candidates[i] < 0:
                    break
                deque.append(candidates[i])
                backtrack(candidates, i+1, end, target - candidates[i], deque)
                deque.pop()
        backtrack(candidates, 0, n, target, deque)
        return ans
# @lc code=end
