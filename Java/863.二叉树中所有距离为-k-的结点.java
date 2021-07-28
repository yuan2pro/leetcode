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
 * @Date         : 2021-07-28 11:28:07
 * @LastEditTime : 2021-07-28 21:34:33
 * @LastEditors  : Do not edit
 * @FilePath     : /Java/863.二叉树中所有距离为-k-的结点.java
 * @Description  : 
 */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode.cn id=863 lang=java
 *
 * [863] 二叉树中所有距离为 K 的结点
 */

// @lc code=start
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {

    Map<Integer, TreeNode> map = new HashMap<>();
    List<Integer> ans = new ArrayList<>();

    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        findParent(root);
        findAns(target, null, 0, k);
        return ans;

    }

    public void findAns(TreeNode node, TreeNode from, int depth, int k) {
        if (node == null) {
            return;
        }
        if (depth == k) {
            ans.add(node.val);
            return;
        }
        // 左儿子儿子深度遍历搜索
        if (node.left != from) {
            findAns(node.left, node, depth + 1, k);
        }
        // 右儿子节点深度遍历搜索
        if (node.right != from) {
            findAns(node.right, node, depth + 1, k);
        }
        // 父节点深度遍历搜索
        if (map.get(node.val) != from) {
            findAns(map.get(node.val), node, depth + 1, k);
        }
    }

    public void findParent(TreeNode root) {
        if (root.left != null) {
            map.put(root.left.val, root);
            findParent(root.left);
        }
        if (root.right != null) {
            map.put(root.right.val, root);
            findParent(root.right);
        }
    }
}
// @lc code=end
