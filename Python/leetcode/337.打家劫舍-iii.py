#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def _rob(root):
            if not root:
                return 0, 0
            ls, ln = _rob(root.left)
            rs, rn = _rob(root.right)
            return root.val + ln + rn, max(ls + ln, rs + rn)
    return max(_rob(root))
        
# @lc code=end

