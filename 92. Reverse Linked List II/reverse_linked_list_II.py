class Node:
  def __init__(self, val = 0,  next = None):
    self.val = val
    self.next = next

class Solution:
  def reverseBetween(self, head, left, right):
     # Handle the edge case where no reversal is needed.
        if not head or left == right:
            return head

        # Use a dummy node to simplify handling the case where left = 1.
        dummy = Node(0, head)
        left_prev = dummy
        
        # 1. Traverse to the node just before the reversal section.
        for _ in range(left - 1):
            left_prev = left_prev.next
            
        # `current` is the first node of the sublist to be reversed (the left-th node).
        current = left_prev.next
        
        # 2. Reverse the sublist in place.
        # This loop runs `right - left` times.
        for _ in range(right - left):
            node_to_move = current.next
            current.next = node_to_move.next
            node_to_move.next = left_prev.next
            left_prev.next = node_to_move
            
        return dummy.next
