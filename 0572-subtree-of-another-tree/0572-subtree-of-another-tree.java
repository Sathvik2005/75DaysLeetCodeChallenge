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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // If the main tree is null, no subtree can exist
        if (root == null) return false;
        
        // Check if the current tree starting at root is identical to subRoot
        if (isSameTree(root, subRoot)) return true;
        
        // Recursively check the left and right children of the current root
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    private boolean isSameTree(TreeNode p, TreeNode q) {
        // If both nodes are null, they are identical
        if (p == null && q == null) return true;
        
        // If only one is null or the values differ, they are not identical
        if (p == null || q == null || p.val != q.val) return false;
        
        // Recursively check if left and right subtrees are identical
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
