class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        
        # Keep only the k largest elements
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.min_heap, val)
        
        # If adding the new element exceeds size k, remove the smallest
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna