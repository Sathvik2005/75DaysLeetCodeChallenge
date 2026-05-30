"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        # Hash map to store the mapping from original node to cloned node
        old_to_new = {}

        def dfs(curr_node):
            # If node is already cloned, return the clone
            if curr_node in old_to_new:
                return old_to_new[curr_node]
            
            # Create a clone for the current node
            copy = Node(curr_node.val)
            old_to_new[curr_node] = copy
            
            # Recursively clone all neighbors
            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy

        return dfs(node)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna