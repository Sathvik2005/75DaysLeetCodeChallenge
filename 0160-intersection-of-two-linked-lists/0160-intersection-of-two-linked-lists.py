# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        # Traverse both lists
        while pA != pB:
            # If pA reaches the end, switch to headB; else move to next
            pA = pA.next if pA else headB
            # If pB reaches the end, switch to headA; else move to next
            pB = pB.next if pB else headA
            
        return pA
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna