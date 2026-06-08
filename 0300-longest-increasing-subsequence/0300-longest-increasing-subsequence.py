class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        # tails stores the smallest tail of all increasing subsequences of length i+1
        tails = []
        
        for num in nums:
            # Use binary search to find the insertion point
            idx = bisect.bisect_left(tails, num)
            
            # If num is larger than all elements in tails, extend the sequence
            if idx == len(tails):
                tails.append(num)
            # Otherwise, update the existing element to a smaller optimal value
            else:
                tails[idx] = num
                
        return len(tails)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna