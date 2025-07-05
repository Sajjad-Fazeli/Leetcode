class Node:
  def __init(self, value = 0, next = None):
    self.value = value
    self.next = next
class Solution:
  def swapPairs(self, head):
    dummy = Node(0, head)
    prev = dummy

    while prev.next and prev.next.next:
      first = prev.next
      second = prev.next.next
      prev.next = second
      first.next = second.next
      second.next = first
      prev = first
  return dummy.next
