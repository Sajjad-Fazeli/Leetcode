## Complexity Analysis

Let **k** be the number of calls made to the `ping` method.

### Time Complexity: O(1) (Amortized)

- **Adding a request:** Each call to `ping` adds a new request to an internal data structure (e.g., a queue or list). This operation typically takes O(1) time (e.g., `append` to a list or `deque`).
- **Removing old requests:** The algorithm needs to remove all requests older than `t - 3000`. While a single `ping` call might iterate through many elements to remove them, each request is added to the data structure once and removed from it once across all `k` calls. Therefore, the total work for `k` calls to `ping` is proportional to `k`.
- **Counting requests:** Obtaining the count of remaining requests takes O(1) time (e.g., `len()` of a list/deque).

Thus, the amortized time complexity for each `ping` operation is **O(1)**.

### Space Complexity: O(1)

- The internal data structure (e.g., a queue or list) stores requests within a 3000ms window.
- Since `t` is an integer representing milliseconds, the maximum number of requests that can exist simultaneously within any 3000ms window is constant (at most 3001 requests if `t` increments by 1ms at a time).
- This maximum size does not depend on the total number of `ping` calls (`k`).

Therefore, the space required is **O(1)**.
