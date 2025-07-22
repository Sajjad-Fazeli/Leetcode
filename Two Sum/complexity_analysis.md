
## Complexity Analysis

Let $$N$$ be the number of elements in the `nums` array.

*   **Time Complexity:** $$O(N)$$
    *   The most efficient approach involves using a hash map (or dictionary). We iterate through the array once. For each number `x`, we check if `target - x` is already in the hash map. If it is, we found our pair. If not, we add `x` and its index to the hash map.
    *   Hash map lookups and insertions typically take $$O(1)$$ on average. Since we perform these operations for each of the $$N$$ elements, the overall time complexity is $$O(N)$$.

*   **Space Complexity:** $$O(N)$$
    *   In the worst-case scenario, we might need to store up to $$N$$ elements in the hash map if no pair is found until the very end (though the problem guarantees a solution exists). Therefore, the space required by the hash map can grow up to $$N$$ elements, leading to a space complexity of $$O(N)$$.
