class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Create a dummy node to handle edge cases, like removing the head.
        dummy = ListNode(0, head)
        
        # Start both pointers from the dummy node.
        slow = dummy
        fast = dummy
        
        # Step 2: Move the fast pointer n + 1 steps ahead.
        # We move n+1 steps so that when fast reaches the end (None),
        # slow is at the node *before* the one to be deleted.
        for _ in range(n + 1):
            fast = fast.next
            
        # Step 3: Move both pointers in sync until the fast pointer reaches the end.
        while fast is not None:
            slow = slow.next
            fast = fast.next
            
        # Step 4: 'slow' is now pointing to the node right before the target node.
        # Perform the deletion by skipping over the target node.
        slow.next = slow.next.next
        
        # Step 5: The head of the modified list is pointed to by dummy.next.
        return dummy.next
