### Complexity Analysis

Let **N** be the number of nodes in the linked list.

- **Time Complexity: O(N)**  
  The algorithm makes a single pass through the entire linked list. The `current` pointer visits each node at most once, resulting in a linear runtime proportional to the number of nodes.

- **Space Complexity: O(1)**  
  The list is modified in-place using only a constant amount of extra memory. The algorithm uses a single pointer (`current`), and the space required does not depend on the size of the list.
