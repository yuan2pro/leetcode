"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        return self.addList(l, root)

    def addList(self, l, root):
        if not root:
            return []
        l.append(root.val)
        self.addList(l, root.left)
        self.addList(l, root.right)
        return l

    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lista = []

        def rpreorderTraversal(root):
            if root:
                lista.append(root.val)
                rpreorderTraversal(root.left)
                rpreorderTraversal(root.right)

        rpreorderTraversal(root)
        return lista
