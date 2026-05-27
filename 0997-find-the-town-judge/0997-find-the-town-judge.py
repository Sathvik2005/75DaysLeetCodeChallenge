class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        scores = [0] * (n + 1)
        
        for a, b in trust:
            scores[a] -= 1
            scores[b] += 1
            
        for i in range(1, n + 1):
            if scores[i] == n - 1:
                return i
                
        return -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna