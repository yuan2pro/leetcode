#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        ans = []
        dp = []

        def backtrack(root):
            dp.append(root.val)
            if root.left == None and root.right == None:
                ans.append("->".join([str(x) for x in dp]))
            if root.left:
                backtrack(root.left)
            if root.right:
                backtrack(root.right)
            dp.pop()
        backtrack(root)
        return ans
# @lc code=end
