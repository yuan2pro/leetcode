#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start


class Solution:
    def combinationSum3(self, k: int, n: int):
        deque = []
        ans = []

        def backtrack(target, deque, start):
            if len(deque) == k and target == 0:
                ans.append(list(deque))
                return
            if len(deque) == k:
                return
            for i in range(start, 10):
                deque.append(i)
                backtrack(target - i, deque, i + 1)
                deque.pop()
        backtrack(n, deque, 1)
        return ans


# @lc code=end
