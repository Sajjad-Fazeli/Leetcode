# Complexity Analysis
## Time Complexity: `O(n)`.
This might seem confusing because of the while loop inside the for loop. However, each index is added to the deque exactly once and removed from the deque at most once. Therefore, over the entire run, the total number of deque operations is proportional to n, giving us an amortized O(n) runtime.
## Space Complexity: `O(k)`.
In the worst-case scenario (a strictly decreasing array), the deque could hold up to k indices at one time.
