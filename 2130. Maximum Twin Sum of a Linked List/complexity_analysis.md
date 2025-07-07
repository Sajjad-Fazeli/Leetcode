# Time Complexity: O(n)

Finding the middle: You use a slow and a fast pointer, traversing the list until the fast pointer reaches the end. This is effectively a single pass and takes *O(n)* time.
Reversing the second half: You reverse the portion of the list from the middle to the end. Since this is half the list, it takes *O(n/2)* time.
Calculating sums: You iterate through the first half and the reversed second half simultaneously. This takes another *O(n/2)* time.
The total time complexity is *O(n + n/2 + n/2)*, which simplifies to **O(n)**. Even though there are multiple steps, each is a linear pass over some or all of the list, so the overall performance is linear.
# Space Complexity: O(1)

This is the key advantage of this approach. You are not creating a new data structure to hold the list's values.
You only use a few extra pointers (slow, fast, prev, curr, etc.) to keep track of nodes during the process. The number of these pointers is constant and does not depend on the size of the linked list.
Therefore, the space complexity is **O(1)**, meaning it uses a constant amount of extra memory regardless of the list's length.
