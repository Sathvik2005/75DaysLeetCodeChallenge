class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution(object):
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            node = root
            for char in w:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = w
        rows, cols = len(board), len(board[0])
        res = []

        # 2. Backtracking function
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            
            curr_node = node.children[char]
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None  # Avoid duplicate entries

            # Mark as visited
            board[r][c] = "#"
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)
            
            # Backtrack (restore character)
            board[r][c] = char

        # 3. Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
                
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna