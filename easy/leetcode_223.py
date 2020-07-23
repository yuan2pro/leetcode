'''
/**
 * 226. 翻转二叉树
 * 翻转一棵二叉树。
 *
 * 示例：
 *
 * 输入：
 *
 *      4
 *    /   \
 *   2     7
 *  / \   / \
 * 1   3 6   9
 * 输出：
 *
 *      4
 *    /   \
 *   7     2
 *  / \   / \
 * 9   6 3   1
 */
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def invertTree2(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)
        # 交换左右子树
        root.left, root.right = root.right, root.left
        return root

    def invertTree1(self, root: TreeNode) -> TreeNode:
        if not root: return None
        queue = [root]
        while queue:
            cur = queue.pop(0)
            cur.left, cur.right = cur.right, cur.left
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
        return root
