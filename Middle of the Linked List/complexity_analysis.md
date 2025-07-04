## Complexity Analysis

Let `N` be the number of nodes in the linked list.

### Time Complexity: O(N)

The algorithm makes a single pass through the linked list. The fast pointer traverses the entire list, while the slow pointer moves through approximately the first half. The total number of operations is directly proportional to `N`.

### Space Complexity: O(1)

Only two extra pointers (`slow` and `fast`) are used. The amount of memory consumed remains constant, regardless of the size of the linked list.
**
