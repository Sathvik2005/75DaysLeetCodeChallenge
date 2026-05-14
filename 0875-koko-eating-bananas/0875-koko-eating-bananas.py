import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        # The range for binary search: 
        # Minimum speed is 1, maximum speed is the largest pile.
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / k)
            
            if hours <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna