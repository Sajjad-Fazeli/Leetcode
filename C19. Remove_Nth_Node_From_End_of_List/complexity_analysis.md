## Complexity Analysis

Let `L` be the number of nodes in the linked list.

### Time Complexity: O(L)

The algorithm requires a single pass through the linked list. The fast pointer traverses the list from beginning to end, while the slow pointer traverses a portion of it. Overall, the total number of steps taken is proportional to `L`.

### Space Complexity: O(1)

Only a few extra pointers are used (`dummy`, `slow`, `fast`). The amount of extra memory used does not depend on the size of the list, so the space complexity is constant.
