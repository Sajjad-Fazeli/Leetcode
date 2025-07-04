from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start a pointer at the head of the list.
        current = head
        
        # We need to loop as long as we have a node AND a node to compare it to.
        while current and current.next:
            # Check if the next node is a duplicate.
            if current.val == current.next.val:
                # If it's a duplicate, skip over the next node.
                # Don't advance 'current' yet, as there might be more duplicates.
                current.next = current.next.next
            else:
                # If it's not a duplicate, move to the next node to continue checking.
                current = current.next
                
        # The list is now modified in-place. Return the head.
        return head

