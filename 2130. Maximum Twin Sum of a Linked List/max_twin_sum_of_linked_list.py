class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        
        # Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse the second half of the linked list
        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            
        # Calculate the maximum twin sum
        max_twin_sum = 0
        left, right = head, prev
        while right:
            max_twin_sum = max(max_twin_sum, left.val + right.val)
            left = left.next
            right = right.next
            
        return max_twin_sum
  
      
      
