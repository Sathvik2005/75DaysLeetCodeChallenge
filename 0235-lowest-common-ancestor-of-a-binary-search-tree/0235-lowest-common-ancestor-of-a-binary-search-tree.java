/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode current = root;
        
        while (current != null) {
            // If both p and q are greater than current, move to the right subtree
            if (p.val > current.val && q.val > current.val) {
                current = current.right;
            } 
            // If both p and q are less than current, move to the left subtree
            else if (p.val < current.val && q.val < current.val) {
                current = current.left;
            } 
            // We found the split point or one of the nodes
            else {
                return current;
            }
        }
        return null;
    }
}
