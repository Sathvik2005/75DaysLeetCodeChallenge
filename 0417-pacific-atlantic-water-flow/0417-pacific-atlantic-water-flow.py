class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or 
                r < 0 or c < 0 or r == rows or c == cols or 
                heights[r][c] < prevHeight):
                return
            
            visit.add((r, c))
            # Check neighbors: up, down, left, right
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Start DFS from top/bottom rows and left/right columns
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])             # Top row (Pacific)
            dfs(rows - 1, c, atl, heights[rows-1][c]) # Bottom row (Atlantic)

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])             # Left col (Pacific)
            dfs(r, cols - 1, atl, heights[r][cols-1]) # Right col (Atlantic)

        # Return coordinates that are in both sets
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna