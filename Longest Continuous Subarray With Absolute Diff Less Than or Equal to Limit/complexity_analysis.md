# Complexity Analysis
## Time Complexity: `O(n)`.
Each element is added to and removed from each deque at most once. The left and right pointers also only traverse the array once. This gives a linear time complexity.
## Space Complexity: `O(n)`. 
In the worst case (e.g., a strictly increasing or decreasing array), the deques could store all n indices.
