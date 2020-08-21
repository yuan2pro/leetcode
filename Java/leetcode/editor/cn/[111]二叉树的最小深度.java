package leetcode.editor.cn;
//给定一个二叉树，找出其最小深度。 
//
// 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。 
//
// 说明: 叶子节点是指没有子节点的节点。 
//
// 示例: 
//
// 给定二叉树 [3,9,20,null,null,15,7], 
//
//     3
//   / \
//  9  20
//    /  \
//   15   7 
//
// 返回它的最小深度 2. 
// Related Topics 树 深度优先搜索 广度优先搜索 
// 👍 340 👎 0


//leetcode submit region begin(Prohibit modification and deletion)

import java.util.LinkedList;
import java.util.Queue;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */
class Solution111_dfs {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) {
            return 1;
        }
        int min_depth = Integer.MAX_VALUE;
        if (root.left != null) {
            min_depth = Math.min(min_depth, minDepth(root.left));
        }
        if (root.right != null) {
            min_depth = Math.min(min_depth, minDepth(root.right));
        }
        return min_depth + 1;
    }
}

class Solution111_bfs {
    class QueueNode {
        TreeNode node;
        int depth;

        public QueueNode(TreeNode node, int depth) {
            this.node = node;
            this.depth = depth;
        }
    }

    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        Queue<QueueNode> queueNodes = new LinkedList<>();
        queueNodes.offer(new QueueNode(root, 1));
        while (!queueNodes.isEmpty()) {
            QueueNode queueNode = queueNodes.poll();
            TreeNode node = queueNode.node;
            int min_depth = queueNode.depth;
            if (node.left == null && node.right == null) {
                return min_depth;
            }
            if (node.left != null) {
                queueNodes.offer(new QueueNode(node.left, min_depth + 1));
            }
            if (node.right != null) {
                queueNodes.offer(new QueueNode(node.right, min_depth + 1));
            }

        }
        return 0;

    }


}


//leetcode submit region end(Prohibit modification and deletion)
