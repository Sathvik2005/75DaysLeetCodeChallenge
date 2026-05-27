class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int

        
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows, cols = len(image), len(image[0])
        start_color = image[sr][sc]
        
        # If the starting pixel is already the target color, no work needed
        if start_color == color:
            return image
        
        def dfs(r, c):
            # Check bounds and if pixel matches the original starting color
            if 0 <= r < rows and 0 <= c < cols and image[r][c] == start_color:
                # Update color
                image[r][c] = color
                
                # Recurse for 4-directional neighbors
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        dfs(sr, sc)
        return image
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna