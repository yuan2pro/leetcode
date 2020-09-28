import leetcode.editor.cn.TreeNode;

/*
 * @lc app=leetcode.cn id=105 lang=java
 *
 * [105] 从前序与中序遍历序列构造二叉树
 */

// @lc code=start
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        TreeNode root = createTree(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1);
        return root;
    }

    private TreeNode createTree(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd) {
        if (preStart > preEnd || inStart > inEnd) {
            return null;
        }
        TreeNode treeNode = new TreeNode(preorder[preStart]);
        for (int i = inStart; i <= inEnd; i++) {
            if (inorder[i] == preorder[preStart]) {
                // 重构左子树
                treeNode.left = createTree(preorder, preStart + 1, preStart + i - inStart, inorder, inStart, i - 1);
                // 重构右子树
                treeNode.right = createTree(preorder, preStart + i - inStart + 1, preEnd, inorder, i + 1, inEnd);
            }
        }
        return treeNode;
    }

}
// @lc code=end
