## Complexity Analysis
### Time Complexity: O(n)

We traverse the list to find the left-1 position. In the worst case, this takes `O(n)` time if left is near the end of the list.
The reversal process itself involves right - left operations.
Since we are essentially making a single pass through the list, the time complexity is linear with respect to the number of nodes, n.
### Space Complexity: O(1)

This algorithm is very memory-efficient. We only use a handful of pointers (dummy, left_prev, current, node_to_move) to perform the reversal.
The amount of extra memory used is constant and does not scale with the size of the input linked list.
