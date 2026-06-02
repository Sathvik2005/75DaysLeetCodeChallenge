class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """ 
        n = len(cost)
        # We can reuse the cost array to save space
        for i in range(2, n):
            cost[i] += min(cost[i-1], cost[i-2])
        
        # The top can be reached from the last or second-to-last step
        return min(cost[n-1], cost[n-2])
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna