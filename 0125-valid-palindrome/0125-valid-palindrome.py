class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filter_char = [char.lower() for char in s if char.isalnum()]
        return filter_char==filter_char[::-1]
        