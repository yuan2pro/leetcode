#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(root, n):
            if not root:
                return
            path.append(root.val)
            n -= root.val
            if not root.left and not root.right and n == 0:
                ans.append(path.copy())
            dfs(root.left, n)
            dfs(root.right, n)
            path.pop()
        dfs(root, sum)
        return ans

# @lc code=end
