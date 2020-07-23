'''
145. 二叉树的后序遍历
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root):
        res = []
        if not root: return res
        src = [root]
        while src:
            p = src.pop()
            res.insert(0, p.val)
            # res.append(p.val)
            if p.left:
                src.append(p.left)
            if p.right:
                src.append(p.right)
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().postorderTraversal(root))
