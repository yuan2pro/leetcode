#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        deque = collections.deque()
        if not root:
            return ans
        while root or deque:
            while root:
                deque.append(root)
                root = root.left
            root = deque.pop()
            ans.append(root.val)
            root = root.right
        return ans


# @lc code=end
