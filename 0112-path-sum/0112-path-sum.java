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
    public boolean hasPathSum(TreeNode root, int targetSum) {
         // Base case: if the tree is empty
        if (root == null) {
            return false;
        }
        
        // Check if the current node is a leaf
        if (root.left == null && root.right == null) {
            return targetSum == root.val;
        }
        
        // Recurse on children with the updated targetSum
        int remainingSum = targetSum - root.val;
        return hasPathSum(root.left, remainingSum) || 
               hasPathSum(root.right, remainingSum);
    }
}