from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counts = Counter(tasks).values()
        
        # 2. Find the maximum frequency
        f_max = max(counts)
        
        # 3. Find how many tasks have that maximum frequency
        k = list(counts).count(f_max)
        
        # 4. Calculate the minimum intervals based on the bottleneck
        # (f_max - 1) groups of (n + 1) size, plus the k tasks in the last group
        min_intervals = (f_max - 1) * (n + 1) + k
        
        # 5. The answer is the larger of the formula result or total tasks
        return max(min_intervals, len(tasks))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna