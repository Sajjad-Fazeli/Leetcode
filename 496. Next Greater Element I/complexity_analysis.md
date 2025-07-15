# Complexity Analysis
## Time Complexity: `O(n + m)`, where n is the length of nums2 and m is the length of nums1. We iterate through nums2 once and nums1 once. Although there is a while loop inside the for loop, each element of nums2 is pushed onto and popped from the stack at most once, making the first part `O(n)`.
## Space Complexity: `O(n)`. In the worst case (e.g., a strictly decreasing nums2), the stack and the hash map could both store all n elements from nums2.
