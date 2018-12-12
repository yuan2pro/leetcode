"""
 Symmetric Tree

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        level = [root]
        while level:
            for i in range(len(level) // 2):
                if level[i] and level[~i]:
                    if level[i].val != level[~i].val:
                        return False
                elif level[i] or level[~i]:
                    return False
            new_level = []
            for node in level:
                if node:
                    new_level.extend([node.left, node.right])
            level = new_level
        return True
