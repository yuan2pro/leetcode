import javax.swing.tree.TreeNode;

/*
 *                   江城子 . 程序员之歌
 * 
 *               十年生死两茫茫，写程序，到天亮。
 *                   千行代码，Bug何处藏。
 *               纵使上线又怎样，朝令改，夕断肠。
 * 
 *               领导每天新想法，天天改，日日忙。
 *                   相顾无言，惟有泪千行。
 *               每晚灯火阑珊处，夜难寐，加班狂。
 * 
 * 
 * @Author       : William
 * @Date         : 2021-07-27 10:51:54
 * @LastEditTime : 2021-07-28 21:42:42
 * @LastEditors  : Do not edit
 * @FilePath     : /Java/671.二叉树中第二小的节点.java
 * @Description  : 
 */

/*
 * @lc app=leetcode.cn id=671 lang=java
 *
 * [671] 二叉树中第二小的节点
 */

// @lc code=start
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode() {} TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left
 * = left; this.right = right; } }
 */
class Solution {
    public int findSecondMinimumValue(TreeNode root) {
        if (root == null) {
            return -1;
        }
        Integer[] min = { root.val, null };
        inorder(root, min);
        return (min[1] == null) ? -1 : min[1];
    }

    public void inorder(TreeNode root, Integer[] min) {
        if (root == null) {
            return;
        }
        if (((root.val != min[0]) && (min[1] == null)) || ((min[0] < root.val) && (root.val < min[1]))) {
            min[1] = root.val;
        } else if (root.val == min[0]) {
            inorder(root.left, min);
            inorder(root.right, min);

        }
    }

}
// @lc code=end
