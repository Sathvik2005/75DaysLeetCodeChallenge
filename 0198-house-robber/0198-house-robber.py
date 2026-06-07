class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev1 = 0  # Max profit up to the previous house
        prev2 = 0  # Max profit up to two houses ago
        
        for num in nums:
            # Decide whether to rob the current house or skip it
            current = max(prev1, prev2 + num)
            
            # Update variables for the next iteration
            prev2 = prev1
            prev1 = current
            
        return prev1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna