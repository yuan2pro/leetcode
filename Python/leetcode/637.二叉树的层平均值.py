#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        a = [root]
        ans = [root.val]
        b = []
        while a:
            k = a.pop(0)
            if k.left:
                b.append(k.left)
            if k.right:
                b.append(k.right)
            if not a:
                n = len(b)
                if n > 0:
                    v = 0
                    while b:
                        x = b.pop(0)
                        v += x.val
                        a.append(x)
                    ans.append(v / n)
        return ans


# @lc code=end
