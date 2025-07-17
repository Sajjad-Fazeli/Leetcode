# Time Complexity: `O(n)`

In the worst-case scenario, the algorithm must visit every node `(n)` once to check all root-to-leaf paths.
# Space Complexity: `O(h)`

The memory usage is determined by the depth of the recursion call stack, which equals the height `(h)` of the tree.
This becomes `O(n)` in the worst case (a completely unbalanced, skewed tree) and O(log n) in the best case (a completely balanced tree).
