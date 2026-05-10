class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [] # Stores indices
        max_area = 0
        # Append a 0 to heights to ensure all bars are processed at the end
        heights.append(0)
        
        for i, h in enumerate(heights):
            # While current height is less than the height of the bar at stack top
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                # If stack is empty, the width is the current index 'i'
                # Otherwise, it's the distance between current index and the new top
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            
            stack.append(i)
            
        # Optional: remove the 0 we added to keep the input list unchanged
        heights.pop()
        return max_area

        