class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        if len(nums) == 1:
            return nums[0]
        
        # Helper function to solve the standard linear House Robber problem
        def rob_linear(houses):
            prev2 = 0  # Max money up to two houses ago
            prev1 = 0  # Max money up to the previous house
            
            for money in houses:
                # Decide to either rob the current house + prev2, or skip it and keep prev1
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current
                
            return prev1

        # Return the maximum of excluding the last house OR excluding the first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna