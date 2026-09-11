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
    public boolean isValidBST(TreeNode root) {
        //-2^31 ---- root val ------ +2^31+1
        return validateBST(root,Long.MIN_VALUE,Long.MAX_VALUE);
    }
    private boolean validateBST(TreeNode root,long low,long high){
        //to avoid null pointer exception
        if(root==null) return true;
        //value out of range
        if(root.val<=low|| root.val >=high) return false;
        boolean left = validateBST(root.left,low,root.val);
        boolean right = validateBST(root.right,root.val,high);
        return left&&right;
    }
}
