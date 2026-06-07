class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        if not s:
            return ""
            
        start, end = 0, 0
        
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Returns the length of the valid palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Check odd-length palindromes (single character center)
            len1 = expand_around_center(i, i)
            # Check even-length palindromes (between two characters center)
            len2 = expand_around_center(i, i + 1)
            
            max_len = max(len1, len2)
            
            # Update the longest boundaries if a larger palindrome is found
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna