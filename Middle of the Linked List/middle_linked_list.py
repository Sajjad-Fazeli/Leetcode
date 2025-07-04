class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        # The loop continues as long as the fast pointer has not reached the end.
        # 'fast' checks for the even case (fast becomes None).
        # 'fast.next' checks for the odd case (fast lands on the last node).
        while fast is not None and fast.next is not None:
            # Move slow pointer one step.
            slow = slow.next
            # Move fast pointer two steps.
            fast = fast.next.next
            
        return slow
