"""

Validate Binary Search Tree

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root, lessThan=float('inf'), largerThan=float('-inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))

    def isValidBST1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def bst_check(node, less_than, greater_than):

            if not node:
                return True

            val = node.val
            left = node.left
            right = node.right

            # check value is according to bst
            if val >= less_than:
                return False
            if val <= greater_than:
                return False

            return bst_check(left, val, greater_than) and bst_check(right, less_than, val)

        return bst_check(root, float('inf'), float('-inf'))
