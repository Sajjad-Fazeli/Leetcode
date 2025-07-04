
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

## Complexity Analysis

### Time Complexity
**Overall time complexity:** `O(n)`, where `n` is the number of nodes in the linked list.

### Space Complexity

- The algorithm only uses two pointers regardless of input size.
- No extra data structures are required.

**Overall space complexity:** `O(1)` (constant space).


# Using Hashmap
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
