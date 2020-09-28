import leetcode.editor.cn.TreeNode;

/*
 * @lc app=leetcode.cn id=106 lang=java
 *
 * [106] 从中序与后序遍历序列构造二叉树
 */

// @lc code=start
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        TreeNode treeNode = createTree(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1);
        return treeNode;
    }

    private TreeNode createTree(int[] inOrder, int inStart, int inEnd, int[] postOrder, int postStart, int postEnd) {
        if (inStart > inEnd || postStart > postEnd) {
            return null;
        }
        TreeNode node = new TreeNode(postOrder[postEnd]);
        for (int i = inStart; i <= inEnd; i++) {
            if (inOrder[i] == postOrder[postEnd]) {
                node.left = createTree(inOrder, inStart, i - 1, postOrder, postStart, postStart + i - inStart - 1);
                node.right = createTree(inOrder, i + 1, inEnd, postOrder, postStart + i - inStart, postEnd - 1);
            }
        }
        return node;
    }
}
// @lc code=end
