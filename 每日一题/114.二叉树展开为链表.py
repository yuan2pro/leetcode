#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        qu = [root]
        while qu:
            q = qu.pop()
            if q.right:
                qu.append(q.right)
                q.right = None
            if q.left:
                qu.append(q.left)
                q.left = None
            if qu:
                q.right = qu[-1]
# @lc code=end
