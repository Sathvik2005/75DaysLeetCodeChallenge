class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                # Build the number k
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the string built so far and the multiplier
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop the previous state
                prev_string, num = stack.pop()
                current_string = prev_string + (num * current_string)
            else:
                # Standard character
                current_string += char
                
        return current_string

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna