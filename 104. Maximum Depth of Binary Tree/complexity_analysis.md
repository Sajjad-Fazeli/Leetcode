# Maximum Depth of Binary Tree

*   **Time Complexity:** $$O(N)$$
    *   To find the maximum depth, we must visit each node in the tree exactly once. This is achieved by any standard tree traversal algorithm (e.g., Depth-First Search or Breadth-First Search). Therefore, the time complexity is directly proportional to the number of nodes.

*   **Space Complexity:** $$O(H)$$
    *   **Recursive Approach (DFS):** The space complexity is determined by the maximum depth of the recursion stack. In the worst-case scenario (a skewed tree, resembling a linked list), the height $$H$$ can be equal to the number of nodes $$N$$. In the best-case scenario (a perfectly balanced tree), the height $$H$$ is approximately $$\log N$$. Thus, the space complexity ranges from $$O(\log N)$$ to $$O(N)$$, which is generally expressed as $$O(H)$$.
    *   **Iterative Approach (BFS):** The space complexity is determined by the maximum number of nodes that can be present in the queue at any given time. In the worst-case scenario (a complete binary tree), the last level can contain up to approximately $$N/2$$ nodes, which means the queue could hold $$O(N)$$ nodes.
