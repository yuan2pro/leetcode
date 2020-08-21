#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
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
    def minDepth_dfs(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        min_depth = 10**9
        if root.left != None:
            min_depth = min(min_depth, self.minDepth(root.left))
        if root.right != None:
            min_depth = min(min_depth, self.minDepth(root.right))
        return min_depth + 1

    def minDepth_bfs(self, root: TreeNode) -> int:
        if root == None:
            return 0
        que = collections.deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))
        return 0

        # @lc code=end
