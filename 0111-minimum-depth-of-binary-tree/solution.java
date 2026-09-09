/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        
        // If left child is null, recurse down the right subtree
        if (root.left == null) {
            return 1 + minDepth(root.right);
        }
        
        // If right child is null, recurse down the left subtree
        if (root.right == null) {
            return 1 + minDepth(root.left);
        }
        
        // If both children exist, take the minimum of both depths
        int ld = minDepth(root.left);
        int rd = minDepth(root.right);
        return 1 + Math.min(ld, rd);
    }
}
