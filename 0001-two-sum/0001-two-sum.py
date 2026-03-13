class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m={}
        for i,n in enumerate(nums):
            c=target-n
            if c in m:
                return [m[c],i]
            m[n]=i
        