# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Iterate while there are nodes in l1 or l2, or a carry exists
        while l1 or l2 or carry:
            # Get values from nodes, defaulting to 0 if list is exhausted
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = v1 + v2 + carry
            carry = total // 10
            val = total % 10
            
            # Create new node with the digit and move pointer
            current.next = ListNode(val)
            current = current.next
            
            # Move to next nodes in input lists if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna