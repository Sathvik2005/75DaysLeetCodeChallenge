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
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;
        
        while (current != null || !stack.isEmpty()) {
            // 1. Reach the leftmost node of the current subtree
            while (current != null) {
                stack.push(current);
                current = current.left;
            }
            
            // 2. Process the node
            current = stack.pop();
            k--; 
            
            // If k reaches 0, we've found the kth smallest element
            if (k == 0) return current.val;
            
            // 3. Move to the right subtree
            current = current.right;
        }
        
        return -1;
    }
}