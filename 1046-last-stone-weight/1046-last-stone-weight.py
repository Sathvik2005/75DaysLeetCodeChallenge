class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # Convert all stones to negative to use heapq as a max-heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            # Extract the two heaviest stones (smallest negative values)
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)
            
            # If they are not equal, the difference remains
            if first != second:
                heapq.heappush(max_heap, first - second)
        
        # If a stone remains, return its positive value; otherwise return 0
        return -max_heap[0] if max_heap else 0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna