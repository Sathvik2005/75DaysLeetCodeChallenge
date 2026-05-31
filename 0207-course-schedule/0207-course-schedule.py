from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # 1. Build the graph and in-degree array
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1
            
        # 2. Queue all nodes with 0 in-degree
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # 3. Process the queue
        visited_count = 0
        while queue:
            curr = queue.popleft()
            visited_count += 1
            
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 4. If visited_count equals total courses, no cycle exists
        return visited_count == numCourses


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna